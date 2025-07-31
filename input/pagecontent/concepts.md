These are the core terms used in this specification. These are largely inspired by **TOGAF/ArchiMate**, and **OpenHIE**. The glossary is grouped into layers, with examples from **Healthcare Supply Chain** and **Client Registry**.

---

## Business Layer

### Architecture Principle
>  A normative statement that guides design or decision-making within an architecture. Principles are high-level rules or guidelines that are enduring and tied to the organization's mission, reflecting values, governance expectations, or desired outcomes.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Ordering systems SHOULD be able to function offline and synchronize when reconnected."_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Essential product data SHALL conform to international coding standards (e.g., GS1, WHO ATC)."_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Client identity resolution SHOULD support both deterministic and probabilistic matching."_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Interoperability between systems SHALL be achieved using standards such as HL7 FHIR and IHE profiles where available."_



### Goal
> A long-term strategic aim that guides the organization’s direction.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Ensure uninterrupted availability of essential medicines." (`No Stock-Out`)_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Ensure unique and consistent identification of patients across all health services."_

---

### Outcome
> A measurable result aligned with a goal, often as a result or effect of a change.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"% of health facilities reporting zero essential stock-outs quarterly."_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"% of patient records correctly matched across systems."_

---

### Business Capability
> A high-level ability of the organization to perform a specific task or achieve an outcome, supported by people, process, and tools.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Supply Chain Management"_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Patient Identity Management"_

---

### Bunsiness Function
> A unit of business capability at any level of granularity; a high-level grouping of business behavior performed to fulfill a capability.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Inventory Monitoring"; "Traceability"_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Client Record Matching"; "Demographic Updates"_

---

### Business Process
> A sequence of application-supported steps that automate or enable a business process.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:
_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Submit Stock Report"; "Reorder Workflow"; "Order Fulfillment"_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Register New Client"; "Update Demographics"; "Client Matching / De-duplication"_

---

### Business Role
> A business responsibility assigned to actors.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Warehouse Manager"; "Supply Chain Officer"_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Patient Registrar"; "Health Information Clerk"_

---

### Business Object (Information)
> A key concept or entity relevant to business operations.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Order"; "Facility"; "Stock Level"_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Client Identifier"; "Person"; "Patient Record"_

---

## Application Layer

### Requirement
> A functional or non-functional condition the application must satisfy to support business needs.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Track and report real-time stock levels per facility."; "Enable SMS-based order submission where internet is unavailable."_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Support identity deduplication and merge of duplicate client records."; "Expose patient search and match via FHIR Patient resource."_

---

### Application Component
> A modular software unit that provides specific functionality.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Logistics Management Information System (LMIS)"; "Product Catalog Service"; "Patient Demographics Query (PDQ) Service"_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Health Worker Registry"; "Client Registry (OpenCR)"_

---

### Data Structure (Logical Model)
> A structured representation of domain concepts used by application components.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _`StockLevelReport`; `SupplyRequest`; `ProductCatalogItem`; `ShipmentNotice`_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _`PatientIdentifier`; `PersonName`_ `PatientDemographics`_

---

## Technology Layer

### Technical Requirement
> A constraint or need on infrastructure to support applications and interoperability.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Support IHE PHARM-110 transaction", "Ensure end-to-end TLS 1.3 encryption"_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Support HL7 FHIR R4 Patient resource", "Enable matching via IHE PIXm/PDQm transactions"_

---

### Data Specification
> A technical specification for data exchange.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples (FHIR Profiles and Interop Specs):_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _`InventoryReport`; `SupplyRequest` (for stock requisition); `Location` (facility registry); `Organization` (supplier info); `Bundle`_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _IHE mCSD (for facility registry sync); IHE PIXm / PDQm (for client registry interoperability)_

---

## Information Layer (Healthcare-specific)

### Vocabulary / Terminology
> Code systems and value sets used to ensure semantic interoperability.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _GS1 Product Codes; WHO ATC Classification; ISO 3166 Country Codes_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _HL7 v3 NullFlavor (for unknown/masked data); Custom value sets for: Gender, Marital Status, Occupation, National Person Identifier formats_

---
