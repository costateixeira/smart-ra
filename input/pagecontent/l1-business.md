# Business Layer

The **Business Layer** defines the strategic and operational foundations of an enterprise. It describes what the organization aims to achieve, how it organizes its operations, and which actors or roles carry out those operations. This layer is independent of technology and focuses on goals, responsibilities, processes, and capabilities.

It serves as the foundation for aligning information systems and technology with the organization’s mission and value delivery.

---

## Purpose

The Business Layer answers the questions:

- **Why** does the organization exist?
- **What** does it want to achieve?
- **How** does it operate to achieve that?
- **Who** is involved in those operations?

These concerns are captured through key architectural concepts.

---

## Key Concepts

### Goal  
A **long-term strategic aim** that guides the organization's direction.

### Outcome  
A **measurable result** aligned with one or more goals.

### Capability  
An **organizational ability** to perform coordinated actions using people, processes, and resources.

### Function  
A **logical grouping of activities** that deliver part of a capability.

### Role  
A **responsibility or behavior** assigned to individuals, organizations, or systems.

### Business Object  
An **informational concept** used in business processes, e.g., _order_, _client_, or _facility_.

---

## Illustrative Example: Client Registry

To make these concepts more concrete, the following example shows how they can be applied in the context of a **Client Registry**, which enables unique identification of patients across healthcare services.

```plantuml
@startuml
skinparam linestyle polyline 

skinparam rectangle<<behavior>> {
	roundCorner 25
}

sprite $bProcess jar:archimate/business-process
sprite $bRole jar:archimate/business-role
sprite $bObject jar:archimate/business-object
sprite $bGoal jar:archimate/motivation-goal
sprite $bOutcome jar:archimate/motivation-outcome
sprite $bCapability jar:archimate/strategy-capability


Package "Outcome and Goals" {
  rectangle "100% Matched\nClient Records" as outcome <<$bOutcome>> #Business
  rectangle "Unique Patient\nIdentification" as goal <<$bGoal>> #Business
}

Package Capabilities {
rectangle "Client Identity Management" as idMgmt <<$bCapability>> #Business
}

package Functions {
    rectangle "Register Client" as regClient <<$bProcess>><<behavior>> #Business
    rectangle "Update Demographics" as updateDemo <<$bProcess>><<behavior>> #Business
'    rectangle "Match / Merge Records" as matchMerge <<$bProcess>><<behavior>> #Business
}

package Roles {
    rectangle "Patient Registrar" as registrar <<$bRole>> #Business
    rectangle "Data Steward" as steward <<$bRole>> #Business
}


Package "Business Objects" {
rectangle "Client Record" as client <<$bObject>> #Business
'rectangle "Client Identifier" as id <<$bObject>> #Business
}

' Relationships
registrar -u-> regClient
steward -u-> updateDemo
'steward --> matchMerge

regClient -u-> idMgmt
updateDemo -u-> idMgmt
'matchMerge --> idMgmt

idMgmt -u-> outcome
outcome -u-> goal

regClient -u-> client
updateDemo -u-> client
'matchMerge --> id
@enduml



```plantuml
@startuml
title Business Layer Metamodel

'skinparam linestyle polyline 

@startuml
skinparam rectangle<<structure>> {
  roundCorner 25
}
skinparam rectangle<<behavior>> {
  roundCorner 25
}
skinparam rectangle<<active>> {
  roundCorner 25
}
skinparam rectangle<<passive>> {
  roundCorner 25
}
skinparam linetype polyline

' ArchiMate sprites
sprite $bRole jar:archimate/business-role
sprite $bFunction jar:archimate/business-function
sprite $bCapability jar:archimate/strategy-capability
sprite $bObject jar:archimate/business-object
sprite $bGoal jar:archimate/motivation-goal
sprite $bOutcome jar:archimate/motivation-outcome
sprite $bPrinciple jar:archimate/principle

' Definitions
rectangle "Principle" as Principle <<$bPrinciple>><<structure>> #Business
rectangle "Goal" as Goal <<$bGoal>><<structure>> #Business
rectangle "Outcome" as Outcome <<$bOutcome>><<structure>> #Business
rectangle "Capability" as Capability <<$bCapability>><<structure>> #Business
rectangle "Function" as Function <<$bFunction>><<behavior>> #Business
rectangle "Role" as Role <<$bRole>><<active>> #Business
rectangle "Business Object" as Info <<$bObject>><<passive>> #Business

' Relationships
Principle -right-> Goal : influences
Goal -r-> Outcome : leads to
Goal -down-> Capability : motivates
Capability -down-> Function : realized by
Function -down-> Info : uses
Role -left-> Function : performs
Role -u-> Capability : supports
Info -up-> Role : managed by

legend left
Metamodel of Business Layer Concepts  
based on TOGAF / ArchiMate core relationships
====
<$bPrinciple> : principle  
<$bGoal> : business goal  
<$bOutcome> : business outcome  
<$bCapability> : capability  
<$bFunction> : function  
<$bRole> : role  
<$bObject> : business object  
endlegend
@enduml
