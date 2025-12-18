# Artifact Index - Reference Architecture v0.2.0

* [**Table of Contents**](toc.md)
* [**Indices**](indices.md)
* **Artifact Index**

## Artifact Index

This page provides a list of the FHIR artifacts defined as part of this implementation guide.

### Requirements: Actor Definitions 

The following artifacts define the types of individuals and/or systems that will interact as part of the use cases covered by this implementation guide.

| | |
| :--- | :--- |
| [Client Registry](ActorDefinition-ClientRegistry.md) | The Client Registry assists in uniquely identifying individuals who receive health care services by: Maintaining a central registry of all patients and their demographics and assigning a unique identifier to each patient.Linking patient registration entries that result due to changes in patient demographics (patient moved to another location), data entry errors during patient registration, or missing demographic information.Enabling health care workers to identify facilities at which a patient has received care. |
| [Facility Registry](ActorDefinition-FacilityRegistry.md) | A registry that stores and manages standardized information about health facilities, serving as a central authority for facility data. |
| [Health Management Information System](ActorDefinition-HealthManagementInformationSystem.md) | A system that collects, analyzes, and reports health data for monitoring and decision-making purposes. |
| [Health Worker Registry](ActorDefinition-HealthWorkerRegistry.md) | A registry that maintains information about health workers, including their identifiers, roles, and affiliations.The Health Worker Registry serves as an authority for maintaining the unique identities of health workers within a context.* Pulls the minimum dataset of health workforce information from the various source data systems.
 
* Merges the source data systems into an authoritative registry of health workers according to a data governance policy. 
 
* Allows queries of health worker information by client systems.
 |
| [Interoperability Layer](ActorDefinition-InteroperabilityLayer.md) | A component that enables communication of services across domains and organizations, This MMAY include:* Service discovery and identification
* Service identity life cycle management
* Encryption of service to service communications
* Authentication, authorization and permissions at the service level (not application or user level)
* Service monitoring and transaction logging
Depending on the governance requirements, this layer may also include tools to centralize service logic including message routing, workflow and service orchestration, and message translation. |
| [Logistics Management Information System](ActorDefinition-LogisticsManagementInformationSystem.md) | A system that manages the supply chain operations, including tracking and distribution of health commodities. |
| [Point-of-Service System](ActorDefinition-PointOfServiceSystem.md) | A system used at the point of care, such as electronic medical records (EMRs), to capture and manage patient encounters and clinical data. |
| [Shared Health Record](ActorDefinition-SharedHealthRecord.md) | A centralized repository that stores and manages longitudinal patient health records, enabling access to clinical data across systems. |
| [Terminology Service](ActorDefinition-TerminologyService.md) | A service that provides access to standardized code systems, value sets, and mappings to ensure consistent use of terminology across systems. |

