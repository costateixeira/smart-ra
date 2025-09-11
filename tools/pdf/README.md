# Reference Architecture PDF Generator — README

A tiny ReportLab-based tool that produces a **WHO-style, navigable reference** for a TOGAF/ArchiMate-style architecture. It creates a booklet with side **tabs** (colored by layer), **typed relationship tables**, simple **diagrams**, and **cross-links** with **page numbers**.

---

## Features

- **Section tabs** on page edges  
  - Business (pale yellow), Application (pale blue), Technology (pale green).  
  - Tabs switch automatically per section: **Business Goals**, **Business Processes**, **Application Components**, **Technology Components**.
- **Flow within sections**: multiple items of the same type share a page; page breaks occur **only between sections**.
- **Typed relationships** (ArchiMate-style wording) shown in two tables per item:  
  - **Business relationships** (yellow header)  
  - **Application relationships** (blue header)
- **Auto-links with page numbers**: any reference to a known ID becomes a clickable link with “(p. N)”.
- **Two-pass build** so links include final page numbers.
- **Vector diagrams** (no `renderPM` / `rlPyCairo` dependency).

---

## Quick start

1. **Install**
   ```bash
   python -m venv .venv
   . .venv/Scripts/activate  # Windows
   # or: source .venv/bin/activate (macOS/Linux)

   pip install -r requirements.txt
   ```
   `requirements.txt`
   ```
   reportlab>=4.1.0
   PyYAML>=6.0.1
   ```

2. **Run**
   ```bash
   python ra_gen.py your_model.yaml out.pdf
   ```

3. **Open** `out.pdf`.

---

## YAML schema

Top-level keys:

```yaml
total_tabs: 12        # optional; how many tab slots vertically
tab_rows:             # optional; tab row per layer
  business: 1
  application: 2
  technology: 3

items:
  - type: goal | process | component | technology
    id: BG-01                # required, used for anchors/links
    type_display: Business Goal
    title: Ensure Unique Patient Identification
    description: >
      Free text. You can include IDs like AC-01 or BP-01; they’ll be auto-linked.
    # TYPED relationships (preferred):
    business_relations:
      - type: realized by    # free text; you can use ArchiMate vocabulary
        id: BP-01            # target ID (must exist in items to be clickable)
        label: Patient Registration  # optional human label (shown in table)
    application_relations:
      - type: implemented by
        id: AC-01
        label: Master Patient Index

    # Legacy fields (still supported; mapped to default phrases):
    processes:      # list of {id, title}
      - { id: BP-01, title: Patient Registration }
    applications:   # list of {id, title}
      - { id: AC-01, title: Master Patient Index }
    supports_goal:      # {id, title}
    supports_process:   # {id, title}

    # Optional cross-refs (all auto-linked if IDs exist)
    dependencies: [AC-01, {ref: BP-01, label: Patient Registration}]   # list (strings or {ref,label})
    impacts:      [BP-02]
    references:   ["HL7 FHIR R4", "OpenHIE CR"]
```

### Relationship typing
- Prefer `business_relations` and `application_relations` with a **`type`** property (e.g., *realized by*, *served by*, *influences*, *supports*, *implemented by*).  
- If you only use legacy fields, the generator maps them to defaults (e.g., Goal→Process = *supported by*, Goal→Component = *implemented by*, etc.).

---

## Output anatomy

- **Section title** (e.g., “Business Goals”).  
- **Item header**: `<Type Display>: <ID> <Title>`  
- **Description**: with auto-linked IDs and page numbers.  
- **Mini diagram**: high-level boxes (for quick orientation).  
- **Business relationships** table: **Type | Target | Link**  
- **Application relationships** table: **Type | Target | Link**  
- **Dependencies / Impacts / References** (inline links).

---

## Customization

- **Tab positions**: change `tab_rows` at YAML root.  
- **Tab colors**: edit `PALE_COLORS` in `ra_gen.py`.  
- **Section order**: change `SECTION_ORDER` in `ra_gen.py`.  
- **Relationship wording**: set `type` strings in YAML (recommended).  
- **Diagrams**: tweak `goal_diagram`, `process_diagram`, `component_diagram` functions.

---

## File reference

- `ra_gen.py` – main generator (v4.1):  
  - Deferred tab meta via `SetSectionMeta` + `handle_pageBegin()`  
  - Two-pass build for page numbers  
  - Typed relationship tables (`add_typed_relationship_table`)  
  - Robust link creation (only when target ID exists)
- `requirements.txt` – dependencies

---

## Troubleshooting

### “LayoutError … tallest row … too large”
- Fixed by **rendering the table title as a paragraph above the table** and using:
  - `wordWrap="CJK"` in paragraph styles,
  - `splitByRow=1` and `repeatRows` on tables,
  - soft-wrapping long tokens.  
- If a single table is still huge, it’s likely 100s of rows: split your item’s relationships into logical groups, or we can auto-split by N rows (ask and I’ll add it).

### “missing URL scheme or undefined destination target”
- Caused by a link to an ID not present in `items`.  
- The generator now **guards links**: if the ID isn’t known, it shows plain text instead of a `<link>`.

### “BP-■01” squares in IDs
- That was from injecting soft-wrap hints into IDs. The generator keeps IDs **ASCII-safe** in the **Link** column; only long **labels**/descriptions get soft-wrapped.

### rlPyCairo / renderPM errors
- We do **not** use `renderPM`; diagrams are vector-drawn with `renderPDF`, so you shouldn’t see these.

---

## Example

```bash
python ra_gen.py ra_sample.yaml doc.pdf
```

`ra_sample.yaml` (minimal):

```yaml
items:
  - type: goal
    id: BG-01
    type_display: Business Goal
    title: Ensure Unique Patient Identification
    description: >
      Ensures unique ID. Depends on AC-01; interacts with BP-01.
    business_relations:
      - type: realized by
        id: BP-01
        label: Patient Registration
    application_relations:
      - type: implemented by
        id: AC-01
        label: Master Patient Index

  - type: process
    id: BP-01
    type_display: Business Process
    title: Patient Registration
    application_relations:
      - type: served by
        id: AC-01
        label: Master Patient Index

  - type: component
    id: AC-01
    type_display: Application Component
    title: Master Patient Index
    business_relations:
      - type: supports
        id: BP-01
        label: Patient Registration
```

---

## Tips & extensions

- Want **strict ArchiMate vocabulary**? We can validate `type` strings and warn on unknown ones.  
- Want **page badges** (e.g., “(p. 5)” styled differently)? We can style the link `Paragraph` or move page numbers into a separate column.  
- Want **Technology** section now? Just add `type: technology` items; the green tab row is already wired.

