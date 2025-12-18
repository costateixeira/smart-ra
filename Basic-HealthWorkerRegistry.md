# Resource HealthWorkerRegistry



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "HealthWorkerRegistry",
  "extension" : [
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.url",
      "valueUri" : "http://smart.who.int/ra/ActorDefinition/HealthWorkerRegistry"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.version",
      "valueString" : "0.2.0"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.name",
      "valueString" : "Health Worker Registry"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.title",
      "valueString" : "Health Worker Registry"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.status",
      "valueCode" : "active"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.experimental",
      "valueBoolean" : false
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.date",
      "valueDateTime" : "2025-12-18T05:26:24+00:00"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.publisher",
      "valueString" : "WHO"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.contact",
      "valueContactDetail" : {
        "name" : "WHO",
        "telecom" : [
          {
            "system" : "url",
            "value" : "http://who.int"
          }
        ]
      }
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.description",
      "valueMarkdown" : "A registry that maintains information about health workers, including their identifiers, roles, and affiliations.  \n\r\nThe Health Worker Registry serves as an authority for maintaining the unique identities of health workers within a context.  \n\r\n* Pulls the minimum dataset of health workforce information from the various source data systems.  \n \r\n* Merges the source data systems into an authoritative registry of health workers according to a data governance policy.   \n\r\n* Allows queries of health worker information by client systems.  \n"
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.jurisdiction",
      "valueCodeableConcept" : {
        "coding" : [
          {
            "system" : "http://unstats.un.org/unsd/methods/m49/m49.htm",
            "code" : "001",
            "display" : "World"
          }
        ]
      }
    },
    {
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ActorDefinition.type",
      "valueCode" : "system"
    }
  ],
  "code" : {
    "coding" : [
      {
        "system" : "http://hl7.org/fhir/fhir-types",
        "code" : "ActorDefinition"
      }
    ]
  }
}

```
