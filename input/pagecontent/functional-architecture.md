The **Functional Layer** defines the application-level behaviors and services that implement business capabilities. It bridges the business and technology layers by specifying how systems behave and interact to fulfill business processes.

This architecture defines the **functional scope** of the solution in terms of **application services, components, and their relationships**.

---

## Purpose

The Functional Layer answers the questions:

* **What services** do systems provide to support business processes?
* **How are these services grouped** into logical applications or components?
* **Which workflows** are enabled by these services?

It connects the strategic business view to concrete technical implementations.

---

## Key Concepts

<figure>
  {% include functional-architecture.svg %}
</figure>

### Application Component

A **modular system unit** responsible for performing a set of related functions or services.

### Application Service

A **discrete functionality** offered by an application component to support business processes.




---

## Example: Client Registry Functional Architecture

This section exemplifies the **application-level architecture** of a **Client Registry (CR)**.

The CR is modeled as an **Application Component**, and it **exposes** a set of distinct **Application Services** representing its supported workflows.

---

### Application Components

| ID    | Name            | Description                                                                                                                                                   |
| ----- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AC001 | Client Registry | Core application component responsible for patient identity management, exposing transactional services for demographic data creation, update, and retrieval. |
{:.table-bordered}

---

### Application Services

| ID                 | Name                  | Description                                                                                                            |
| ------------------ | --------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| CRWF-1             | Create Patient Record | Service that supports the creation of a new patient demographic record in the CR.                                      |
| CRWF-2             | Update Patient Record | Service that supports updating an existing patient’s demographic data.                                                 |
| CRWF-3             | Query by Identifier   | Service that allows clients to retrieve a patient record by supplying a unique identifier.                             |
| CRWF-4             | Query by Demographics | Service that enables clients to search for patient records using demographic criteria (e.g., name, birthdate, gender). |
{:.table-bordered}


Each of these services is **exposed by** the `Client Registry` and can be invoked by external systems through defined interfaces (e.g., RESTful APIs, HL7 v3 messages, IHE transactions).

---

### 🔗 Relationships

* The `Client Registry` **exposes** each Application Service directly.
* Each service maps to a **functional transaction** described in the business layer, and can be traced back to the workflows described in the business process model (e.g., "Register New Client", "Update Client Demographics").

---
