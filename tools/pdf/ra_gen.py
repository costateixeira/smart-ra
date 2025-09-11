#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reference Architecture PDF generator (v4.1 — typed relationships + correct tabs + safe tables)
- Page break ONLY between sections (types)
- Tabs change per section using SetSectionMeta -> handle_pageBegin()
- Items within a section share pages (no forced breaks per item)
- Relationship tables are TYPED (ArchiMate-like) and show Type / Target / Link
- Accepts explicit typed relations and maps legacy fields with sensible defaults
- Links only created when targets exist; two-pass build adds page numbers
- Vector diagrams (no renderPM)
- Table safety: CJK wordWrap + soft-wrap long tokens + splitByRow + repeat header
"""

import sys, os, re, yaml, tempfile
from collections import defaultdict
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Flowable,
    Table, TableStyle, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.graphics.shapes import Drawing, Rect, String, Line
from reportlab.graphics import renderPDF
from reportlab.platypus import KeepInFrame

PALE_COLORS = {"business":"#FFF9E5","application":"#EAF2FB","technology":"#E2EFDA"}
TYPE_META = {
    "goal":{"type_display":"Business Goal","layer":"business"},
    "process":{"type_display":"Business Process","layer":"business"},
    "component":{"type_display":"Application Component","layer":"application"},
    "technology":{"type_display":"Technology Component","layer":"technology"},
}
SECTION_ORDER = ["goal","process","component","technology"]

# =============== Utilities ===============

# insert zero-width spaces to make very long tokens wrappable
_ZWSP = "\u200b"
def soft_wrap(text: str, every: int = 24) -> str:
    if not text: return ""
    # Opportunistic breaks after separators and also at fixed intervals
    t = re.sub(r'([/_\-.])', r'\1' + _ZWSP, text)
    # Also inject ZWSP every N chars for long runs without separators
    chunks = []
    run = 0
    for ch in t:
        chunks.append(ch)
        run += 1
        if run >= every:
            chunks.append(_ZWSP)
            run = 0
        if ch in " \t\n":
            run = 0
    return "".join(chunks)

# =============== Styles ===============
def styleset():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle(name="TitleH", fontSize=16, leading=20, spaceAfter=6,
                         textColor=colors.HexColor("#003366")))
    s.add(ParagraphStyle(name="Body", fontSize=11, leading=15, spaceAfter=6, wordWrap="CJK"))
    s.add(ParagraphStyle(name="Muted", fontSize=10, leading=13, textColor=colors.HexColor("#333333"), wordWrap="CJK"))
    s.add(ParagraphStyle(name="SmallHdr", fontSize=11, leading=14, textColor=colors.HexColor("#003366"),
                         spaceBefore=4, spaceAfter=6))
    s.add(ParagraphStyle(name="TableText", fontSize=10, leading=13, wordWrap="CJK"))
    return s


def add_typed_relationship_table(story, title, rows, bg_hex, page_map, styles, known_ids):
    """Render a separate bold title paragraph, then the table with column headers.
       This avoids the 'tallest row' bug seen when the title is inside the table."""
    if not rows:
        return

    # Title above the table (not inside it)
    story.append(Paragraph(f"<b>{title}</b>", styles["SmallHdr"]))

    # Build the table data with a single header row
    header = [
        Paragraph("<b>Type</b>", styles["TableText"]),
        Paragraph("<b>Target</b>", styles["TableText"]),
        Paragraph("<b>Link</b>", styles["TableText"]),
    ]
    data = [header]

    for rtype, label, rid in rows:
        # Link cell (only if ID exists)
        if rid and rid in known_ids:
            pg = page_map.get(rid); suffix = f" (p. {pg})" if pg else ""
            link_html = f'<link href="#{rid}">{(rid)}{suffix}</link>'
            link_cell = Paragraph(link_html, styles["TableText"])
        else:
            link_cell = Paragraph((rid or ""), styles["TableText"])

        data.append([
            Paragraph((rtype or ""), styles["TableText"]),
            Paragraph((label or ""), styles["TableText"]),
            link_cell,
        ])

    # Wider target column; allow row splitting; repeat the single header row
    tbl = Table(
        data,
        colWidths=[120, 300, 62],
        repeatRows=1,
        splitByRow=1,
        hAlign="LEFT",
    )
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor(bg_hex)),  # header bg
        ("TEXTCOLOR", (0,0), (-1,0), colors.HexColor("#003366")),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("OUTLINE", (0,0), (-1,-1), 0.25, colors.lightgrey),
        ("INNERGRID", (0,0), (-1,-1), 0.25, colors.lightgrey),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("TOPPADDING", (0,0), (-1,-1), 4),
    ]))

    # Final safety: keep the table within the frame by shrinking if needed
    kif = KeepInFrame( maxWidth=483, maxHeight=600, content=[tbl], mode='shrink' )
    story.append(kif)

# =============== Tabs ===============
def make_dynamic_tab_template(get_tab_params, total_tabs: int = 12) -> PageTemplate:
    frame = Frame(50, 50, A4[0]-100, A4[1]-100, id='normal')
    def draw_tab(canvas, doc):
        meta = get_tab_params(canvas, doc)
        color_hex = meta.get("color_hex", "#FFFFFF"); label = meta.get("label", "Item"); index = int(meta.get("index", 1))
        th = doc.pagesize[1] / float(total_tabs); y = doc.pagesize[1] - (index * th)
        canvas.saveState()
        canvas.setFillColor(colors.HexColor(color_hex)); canvas.rect(doc.pagesize[0]-20, y, 20, th, fill=1, stroke=0)
        canvas.setFillColor(colors.black); canvas.setFont("Helvetica-Bold", 6)
        canvas.saveState(); canvas.translate(doc.pagesize[0]-15, y + th/2.0); canvas.rotate(90)
        canvas.drawCentredString(0, 0, str(label)); canvas.restoreState()
        canvas.setFont("Helvetica", 8); canvas.setFillColor(colors.grey)
        canvas.drawCentredString(doc.pagesize[0]/2.0, 20, str(doc.page))
        canvas.restoreState()
    return PageTemplate(id="dynamic_tab", frames=[frame], onPage=draw_tab)

class SectionDocTemplate(BaseDocTemplate):
    def __init__(self, filename, total_tabs=12, **kwargs):
        super().__init__(filename, **kwargs)
        self._current_meta = {"color_hex":"#FFFFFF","label":"Item","index":1}
        self._pending_meta = None
        self._anchor_pages = {}  # id -> page
        self.addPageTemplates([ make_dynamic_tab_template(lambda c,d: self._current_meta, total_tabs) ])

    def handle_pageBegin(self):
        # apply pending meta at the start of a new page, before onPage runs
        if self._pending_meta:
            self._current_meta = self._pending_meta
            self._pending_meta = None
        super().handle_pageBegin()

class SetSectionMeta(Flowable):
    """Schedules new tab meta to apply on the NEXT page."""
    def __init__(self, meta: dict):
        super().__init__(); self.meta = meta
    def wrap(self, aw, ah):
        try:
            self.canv._doctemplate._pending_meta = self.meta
        except Exception:
            pass
        return (0,0)
    def draw(self):  # nothing to draw
        return

class Anchor(Flowable):
    def __init__(self, anchor_id: str):
        super().__init__(); self.anchor_id = anchor_id
    def wrap(self, aw, ah): return (0,0)
    def draw(self):
        self.canv.bookmarkPage(self.anchor_id)
        try: self.canv._doctemplate._anchor_pages[self.anchor_id] = self.canv.getPageNumber()
        except Exception: pass

# =============== Diagrams ===============
class DiagramFlowable(Flowable):
    def __init__(self, drawing: Drawing, width=320, height=150):
        super().__init__(); self.drawing=drawing; self.width=width; self.height=height
    def wrap(self, aw, ah): return (min(self.width, aw), self.height)
    def draw(self):
        dw, dh = float(self.drawing.width), float(self.drawing.height)
        sx = self.width/dw if dw else 1.0; sy = self.height/dh if dh else 1.0
        self.canv.saveState(); self.canv.scale(sx, sy); renderPDF.draw(self.drawing, self.canv, 0, 0); self.canv.restoreState()

def goal_diagram(item, cmap):
    d=Drawing(420,170); biz=colors.HexColor(cmap["business"]); app=colors.HexColor(cmap["application"])
    d.add(Rect(160,120,120,35,strokeColor=colors.black,fillColor=biz,rx=8,ry=8))
    d.add(String(165,135,item.get("id","BG-?"),fontSize=9)); d.add(String(165,123,item.get("title","Goal"),fontSize=8))
    px=60
    for p in item.get("processes",[])[:2]:
        d.add(Rect(px,70,160,32,strokeColor=colors.black,fillColor=biz,rx=8,ry=8))
        d.add(String(px+6,85,p.get("id","BP-?"),fontSize=8)); d.add(String(px+6,73,p.get("title","Process"),fontSize=7)); px+=200
    ax=60
    for a in item.get("applications",[])[:2]:
        d.add(Rect(ax,20,160,32,strokeColor=colors.black,fillColor=app,rx=8,ry=8))
        d.add(String(ax+6,35,a.get("id","AC-?"),fontSize=8)); d.add(String(ax+6,23,a.get("title","Component"),fontSize=7)); ax+=200
    d.add(Line(220,120,140,102)); d.add(Line(220,120,360,102)); d.add(Line(140,70,140,52)); d.add(Line(360,70,360,52)); return d

def process_diagram(item, cmap):
    d=Drawing(420,170); biz=colors.HexColor(cmap["business"]); app=colors.HexColor(cmap["application"])
    d.add(Rect(160,130,120,32,strokeColor=colors.black,fillColor=biz,rx=8,ry=8))
    g=item.get("supports_goal") or {}; d.add(String(165,145,g.get("id","BG-?"),fontSize=8)); d.add(String(165,133,g.get("title","Goal"),fontSize=7))
    d.add(Rect(160,80,120,32,strokeColor=colors.black,fillColor=biz,rx=8,ry=8))
    d.add(String(165,95,item.get("id","BP-?"),fontSize=8)); d.add(String(165,83,item.get("title","Process"),fontSize=7))
    ax=60
    for a in item.get("applications",[])[:2]:
        d.add(Rect(ax,20,160,32,strokeColor=colors.black,fillColor=app,rx=8,ry=8))
        d.add(String(ax+6,35,a.get("id","AC-?"),fontSize=8)); d.add(String(ax+6,23,a.get("title","Component"),fontSize=7)); ax+=200
    d.add(Line(220,130,220,112)); d.add(Line(220,80,140,52)); d.add(Line(220,80,360,52)); return d

def component_diagram(item, cmap):
    d=Drawing(420,170); biz=colors.HexColor(cmap["business"]); app=colors.HexColor(cmap["application"])
    d.add(Rect(140,85,160,32,strokeColor=colors.black,fillColor=app,rx=8,ry=8))
    d.add(String(145,100,item.get("id","AC-?"),fontSize=8)); d.add(String(145,88,item.get("title","Component"),fontSize=7))
    d.add(Rect(160,135,140,32,strokeColor=colors.black,fillColor=biz,rx=8,ry=8))
    p=item.get("supports_process") or {}; d.add(String(165,150,p.get("id","BP-?"),fontSize=8)); d.add(String(165,138,p.get("title","Process"),fontSize=7))
    d.add(Rect(160,185,140,32,strokeColor=colors.black,fillColor=biz,rx=8,ry=8))
    g=item.get("supports_goal") or {}; d.add(String(165,200,g.get("id","BG-?"),fontSize=8)); d.add(String(165,188,g.get("title","Goal"),fontSize=7))
    d.add(Line(220,185,220,167)); d.add(Line(220,135,220,117)); return d

def diagram_for(item):
    t=(item.get("type") or "").strip().lower()
    return goal_diagram(item, PALE_COLORS) if t=="goal" else \
           process_diagram(item, PALE_COLORS) if t=="process" else \
           component_diagram(item, PALE_COLORS) if t=="component" else None

# =============== Linking helpers ===============
ID_RE = re.compile(r'\b([A-Z]{2,4}-\d{2,4})\b')

def autolink_text(text: str, id_title_map: dict, page_map: dict, known_ids: set) -> str:
    if not isinstance(text, str): return ""
    def repl(m):
        _id = m.group(1)
        if _id not in known_ids: return (_id)
        label = id_title_map.get(_id, _ZWSP.join(list(_id)))
        pg = page_map.get(_id); suffix = f" (p. {pg})" if pg else ""
        return f'<link href="#{_id}">{(label)}{suffix}</link>'
    return ID_RE.sub(repl, text)

def para(text, style): return Paragraph(text, style)

# =============== Relationship tables (typed) ===============
DEFAULT_REL = {
    ("goal","process"):       "supported by",
    ("goal","component"):     "implemented by",
    ("process","goal"):       "contributes to",
    ("process","component"):  "served by",
    ("component","process"):  "supports",
    ("component","goal"):     "contributes to",
}

def relationship_rows_for(item, section_type):
    """Return two lists: business_rows, app_rows of tuples (type, label, id)."""
    biz_rows, app_rows = [], []
    t = section_type

    # Explicit typed relations
    for rel in item.get("business_relations", []):
        rid = rel.get("id") or rel.get("target")
        rtype = rel.get("type") or "related to"
        lab = rel.get("label") or rel.get("title") or (rid or "")
        biz_rows.append((rtype, lab, rid))
    for rel in item.get("application_relations", []):
        rid = rel.get("id") or rel.get("target")
        rtype = rel.get("type") or "related to"
        lab = rel.get("label") or rel.get("title") or (rid or "")
        app_rows.append((rtype, lab, rid))

    # Legacy fields → heuristic types
    if t == "goal":
        for p in item.get("processes", []):
            rid = p.get("id"); lab = f'{p.get("title","Process")} ({rid})' if rid else (p.get("title","Process"))
            biz_rows.append((DEFAULT_REL[("goal","process")], lab, rid))
        for a in item.get("applications", []):
            rid = a.get("id"); lab = f'{a.get("title","Component")} ({rid})' if rid else (a.get("title","Component"))
            app_rows.append((DEFAULT_REL[("goal","component")], lab, rid))
    elif t == "process":
        g = item.get("supports_goal")
        if g:
            rid = g.get("id"); lab = f'{g.get("title","Goal")} ({rid})' if rid else (g.get("title","Goal"))
            biz_rows.append((DEFAULT_REL[("process","goal")], lab, rid))
        for a in item.get("applications", []):
            rid = a.get("id"); lab = f'{a.get("title","Component")} ({rid})' if rid else (a.get("title","Component"))
            app_rows.append((DEFAULT_REL[("process","component")], lab, rid))
    elif t == "component":
        sp = item.get("supports_process")
        if sp:
            rid = sp.get("id"); lab = f'{sp.get("title","Process")} ({rid})' if rid else (sp.get("title","Process"))
            biz_rows.append((DEFAULT_REL[("component","process")], lab, rid))
        sg = item.get("supports_goal")
        if sg:
            rid = sg.get("id"); lab = f'{sg.get("title","Goal")} ({rid})' if rid else (sg.get("title","Goal"))
            biz_rows.append((DEFAULT_REL[("component","goal")], lab, rid))

    return biz_rows, app_rows

def typed_relationship_table(title, rows, bg_hex, page_map, styles, known_ids):
    """rows: list of (type, label, id)"""
    if not rows:
        return None

    # Two-row header:
    #  - Row 0: big title spanning all columns
    #  - Row 1: per-column labels
    data = [
        [
            Paragraph(f"<b>{title}</b>", styles["TableText"]),
            Paragraph("", styles["TableText"]),
            Paragraph("", styles["TableText"]),
            Paragraph("", styles["TableText"]),
        ],
        [
            Paragraph("", styles["TableText"]),  # spacer column
            Paragraph("<b>Type</b>", styles["TableText"]),
            Paragraph("<b>Target</b>", styles["TableText"]),
            Paragraph("<b>Link</b>", styles["TableText"]),
        ],
    ]

    for rtype, label, rid in rows:
        # Link cell (only if ID exists)
        if rid and rid in known_ids:
            pg = page_map.get(rid)
            suffix = f" (p. {pg})" if pg else ""
            link_html = f'<link href="#{rid}">{(rid)}{suffix}</link>'
            link_cell = Paragraph(link_html, styles["TableText"])
        else:
            link_cell = Paragraph((rid or ""), styles["TableText"])

        data.append([
            Paragraph("", styles["TableText"]),                   # spacer
            Paragraph(soft_wrap(rtype or ""), styles["TableText"]),
            Paragraph(soft_wrap(label or ""), styles["TableText"]),
            link_cell,
        ])

    # Wider target column; repeat both header rows; allow row splitting
    tbl = Table(
        data,
        colWidths=[8, 110, 300, 62],
        repeatRows=2,
        splitByRow=1,
    )

    tbl.setStyle(TableStyle([
        # Title row background + span across all four columns
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(bg_hex)),
        ("SPAN", (0, 0), (-1, 0)),
        ("ALIGN", (0, 0), (-1, 0), "LEFT"),
        ("VALIGN", (0, 0), (-1, 0), "MIDDLE"),

        # Column-header row background
        ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor(bg_hex)),
        ("TEXTCOLOR", (0, 0), (-1, 1), colors.HexColor("#003366")),
        ("FONTNAME", (0, 0), (-1, 1), "Helvetica-Bold"),

        # Table borders and grids
        ("OUTLINE", (0, 0), (-1, -1), 0.25, colors.lightgrey),
        ("INNERGRID", (0, 1), (-1, -1), 0.25, colors.lightgrey),

        # Cell alignment and padding
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
    ]))

    return tbl


# =============== Build ===============
def build_story(doc, data, page_map):
    styles = styleset()
    items = data.get("items", [])
    grouped = defaultdict(list)
    for it in items:
        t = (it.get("type") or "").strip().lower(); grouped[t].append(it)
    id_title = {it.get("id"): f"{it.get('id')} {it.get('title','')}".strip() for it in items if it.get("id")}
    known_ids = set(id_title.keys())
    story = []
    tab_rows = data.get("tab_rows") or {"business":1,"application":2,"technology":3}

    first_section = True
    for section_type in SECTION_ORDER:
        section_items = grouped.get(section_type, [])
        if not section_items: continue

        meta = TYPE_META[section_type]; label = meta["type_display"]; layer = meta["layer"]
        color_hex = PALE_COLORS[layer]; tab_index = int(tab_rows.get(layer, 1))

        if first_section:
            doc._current_meta = {"color_hex":color_hex,"label":label,"index":tab_index}
            first_section = False
        else:
            story.append(SetSectionMeta({"color_hex":color_hex,"label":label,"index":tab_index}))
            story.append(PageBreak())

        story.append(para(f"{label}s", styles["SmallHdr"]))

        for it in section_items:
            if it.get("id"): story.append(Anchor(it["id"]))
            title = f'{it.get("type_display", label)}: {it.get("id","?")} {it.get("title","")}'.strip()
            story.append(para((title), styles["TitleH"]))

            if it.get("description"):
                story.append(para(autolink_text(it["description"], id_title, page_map, known_ids), styles["Body"]))

            d = diagram_for(it)
            if d: story.append(DiagramFlowable(d, width=320, height=150))

            # Typed relationship tables
            biz_rows, app_rows = relationship_rows_for(it, section_type)
            if biz_rows:
                story.append(Spacer(1,6))
                add_typed_relationship_table(story, "Business relationships", biz_rows, PALE_COLORS["business"], page_map, styles, known_ids)
            if app_rows:
                story.append(Spacer(1,6))
                add_typed_relationship_table(story, "Application relationships", app_rows, PALE_COLORS["application"], page_map, styles, known_ids)

            # Dependencies / Impacts / References
            for sec in ("dependencies","impacts","references"):
                vals = it.get(sec); 
                if not vals: continue
                if not isinstance(vals, list): vals=[vals]
                segs = []
                for v in vals:
                    if isinstance(v, dict) and v.get("ref"):
                        rid=v["ref"]
                        if rid in known_ids:
                            lab=v.get("label") or id_title.get(rid, rid)
                            pg=page_map.get(rid); suf=f" (p. {pg})" if pg else ""
                            segs.append(f'<link href="#{rid}">{(lab)}{suf}</link>')
                        else:
                            segs.append((v.get("label") or rid))
                    elif isinstance(v, str) and v in known_ids:
                        lab=id_title[v]; pg=page_map.get(v); suf=f" (p. {pg})" if pg else ""
                        segs.append(f'<link href="#{v}">{(lab)}{suf}</link>')
                    else:
                        segs.append(autolink_text((str(v)), id_title, page_map, known_ids))
                story.append(para(f'{sec.capitalize()}: ' + "; ".join(segs), styles["Muted"]))

            story.append(Spacer(1,10))
    return story

def make_doc(data, filename):
    return SectionDocTemplate(filename, total_tabs=int(data.get("total_tabs",12)), pagesize=A4)

def build_doc(data: dict, out_pdf: str):
    # Pass 1: collect anchor -> page map
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf"); tmp_path = tmp.name; tmp.close()
    doc1 = make_doc(data, tmp_path)
    story1 = build_story(doc1, data, page_map={})
    doc1.build(story1)
    page_map = doc1._anchor_pages.copy()

    # Pass 2: final build with page numbers in link labels
    doc2 = make_doc(data, out_pdf)
    story2 = build_story(doc2, data, page_map=page_map)
    doc2.build(story2)

def main():
    if len(sys.argv) < 3:
        print("Usage: python ra_gen.py <input.yaml> <output.pdf>")
        sys.exit(1)
    input_yaml, output_pdf = sys.argv[1], sys.argv[2]
    with open(input_yaml, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    os.makedirs(os.path.dirname(output_pdf) or ".", exist_ok=True)
    build_doc(data, output_pdf)

if __name__ == "__main__":
    main()
