# Business View: Client Registry

This page presents the **Business Architecture** for a national or regional **Client Registry**, a foundational capability for integrated, person-centered healthcare.

It defines the key business goals, capabilities, processes, roles, and concepts using terminology aligned with **ArchiMate**, while remaining accessible to business audiences.

> _This model supports alignment with enterprise architecture frameworks such as TOGAF and reference models such as OpenHIE._

---

This page serves as a **business-readable entry point** to the Client Registry Business architecture.

---

## Methodology Note

The example **Client Registry architecture** is documented using:
- **Business-readable concepts** (Goals, Outcomes, Capabilities…)
- **Narrative descriptions**
- **ArchiMate notation for illustration** (but based on structured, machine-readable internal format)
- **Standards alignment** (e.g. FHIR Patient, Identifier, Merge Operation)

This enables:
- Shared understanding across stakeholders of different levels.
- Integration with digital health reference models and the overall Reference Architecture.
- Traceability from strategic goals to technical specifications.

---

## Overview

Business overview: 
<!-- * Business Principle "Accessibility for Stakeholders" (PR001)
→ influences → Business Goal "Ensure unique patient identification" (G001) -->

* Business Goal "Ensure unique patient identification" (G001)  
is _**realized by**_ Business Capability "Patient Identity Management" (C001)

* Business Capability "Patient Identity Management" (C001)  
is _**realized**_ by → Business Function "Client Registration and Search" (F001)

* Business Function "Client Registration and Search" (F001)  
is _**composed of**_ → Business Process "Query by Identifier" (BP003)  
is _**composed of**_ → Business Process "Query by Demographics" (BP004)

* Business Process "Register New Client" (BP001)  
→ uses → Business Object "Client Identity" (BO001)  
is _**assigned to**_ → Business Role "Administrative Health Worker" (BR001)

* Business Process "Update Client Demographics" (BP002)  
→ uses → Business Object "Demographic Data" (BO002)  
is _**assigned to**_ → Business Role "Administrative Health Worker" (BR001)

<!-- * Business Process "Match Records" (BP003)  
→ uses → Business Object "Record Match" (BO003)  
is _**assigned to**_ → Business Role "Data Steward" (BR002)

* Business Process "Merge Records" (BP004)  
→ uses → Business Object "Merge Log" (BO004)  
is _**assigned to**_ → Business Role "Data Steward" (BR002) -->



## ✅ Goals

> Long-term strategic aims that guide the health system’s direction.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Goal001: Ensure unique and consistent identification of patients across all health services."_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Goal002: Enable person-centered care by linking data across health encounters."_  

---

## Outcomes

> Measurable results aligned with the stated goals.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Out001 % of patient records correctly matched across systems"_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Out002 Number of duplicate IDs merged per quarter"_  

---

## 🧠 Capabilities

> High-level organizational abilities supported by people, processes, and technology.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Cap001 Patient Identity Management"_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Cap002 Record Matching and Deduplication"_  

---

## Business Processes (Functions)

> Coherent sets of business behavior that fulfill a capability.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"BP001 Register New Client"_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"BP002 Update Client Demographics"_  
<!-- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"BP003 Perform Record Matching"_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"BP004 Merge Duplicate Records"_   -->

---

## 👤 Roles

> Responsibilities assigned to actors in the business.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"BR001 Administrative Health Worker"_  
<!-- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"BP002 Client Registry Data Steward"_   -->

---

## 🧾 Business Concepts

> Information objects important to the domain.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
- _Client / Patient_  
- _Unique Identifier_  
- _Person Name_  
- _Date of Birth_  
- _Record Match Status_  
<!-- - _Merge Audit Trail_   -->

---

## 🔧 Business View Diagram

This diagram shows the **key business functions and roles** in the Client Registry context using **ArchiMate** notation.

```plantuml
@startuml
skinparam rectangle<<behavior>> {
  roundCorner 25
}

sprite $bProcess jar:archimate/business-process
sprite $bRole jar:archimate/business-role
sprite $bObject jar:archimate/business-object
sprite $bFunction jar:archimate/business-function
sprite $bCapability jar:archimate/strategy-capability
sprite $bGoal jar:archimate/motivation-goal
sprite $bPrinciple jar:archimate/principle

' Core Business Layer
rectangle "[[# Register New Client\n(BP001)]]" as Reg <<$bProcess>><<behavior>> #Business
rectangle "[[# Update Client Demographics\n(BP002)]]" as Update <<$bProcess>><<behavior>> #Business
'rectangle "[[# Match Records\n(BP003)]]" as Match <<$bProcess>><<behavior>> #Business
'rectangle "[[# Merge Records\n(BP004)]]" as Merge <<$bProcess>><<behavior>> #Business

Reg -r-> Update : follows
'Update -down-> Match : triggers
'Match -r-> Merge : triggers


' Roles
'rectangle "[[# Registration Clerk\n(BR001)]]" as Clerk <<$bRole>> #Business
rectangle "[[# Administrative HW\n(BR002)]]" as AdministrativeHW <<$bRole>> #Business

AdministrativeHW -d-> Reg : performs
AdministrativeHW -d-> Update : performs
'Steward -u-> Match : performs
'Steward -u-> Merge : performs

' Objects
rectangle "[[# Demographic Data\n(BO002)]]" as Demographics <<$bObject>> #Business
'rectangle "[[# Record Match\n(BO003)]]" as RecordMatch <<$bObject>> #Business
'rectangle "[[# Merge Log\n(BO004)]]" as MergeLog <<$bObject>> #Business
'Demographics -r[hidden]- RecordMatch

'Demographics -r[hidden]- RecordMatch

Update -down-> Demographics : updates
'Match -down-> RecordMatch : creates
'Merge -down-> MergeLog : creates

' Function and Capability
rectangle "[[# Client Registration & Search\n(F001)]]" as Function <<$bFunction>> #Business
rectangle "[[# Patient Identity Management\n(C001)]]" as Capability <<$bCapability>> #Business

Function -down-> Reg : realizes
Function -down-> Update : realizes
'Function -down-> Match : realizes
'Function -down-> Merge : realizes

Capability -down-> Function : supports

' Goal and Principle
rectangle "[[# Business Goal G001\nEnsure Unique Patient ID]]" as Goal <<$bGoal>> #Business
'rectangle "[[# Accessibility for Stakeholders\n(PR001)]]" as Principle <<$bPrinciple>> #Business

Goal -down-> Capability : enables
'Principle -right-> Goal : motivates

' Legend
legend left
<$bGoal> : Business Goal  
<$bCapability> : Business Capability  
<$bFunction> : Business Function  
<$bProcess> : Business Process  
<$bRole> : Business Role  
<$bObject> : Business Object  
'<$bPrinciple> : Architecture Principle  
endlegend
@enduml



```

---
