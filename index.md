# Home - Reference Architecture v0.2.0

* [**Table of Contents**](toc.md)
* **Home**

## Home

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/ra/ImplementationGuide/smart.who.int.ra | *Version*:0.2.0 |
| Draft as of 2025-12-18 | *Computable Name*:RA |

### Overview

#### Background

Recent abrupt donor funding freezes and sudden program exits have destabilized digital health systems across low- and middle-income countries. This has left governments scrambling to preserve patient records, laboratory networks, and supply chain platforms essential for routine services and disease surveillance systems. The crisis reveals deeper problems: monolithic, externally supported technologies that are not linked to national architectural plans or digital public infrastructure investments, approaches that fail to use global interoperability standards, neglect local software talent, and depend on external financing and technical support.

Digital Public Infrastructure (DPI) is a concept that encompasses shared digital systems that are secure, interoperable, and built on open standards. These systems facilitate equitable access to public services, drive development, and promote innovation. Recognized as a critical enabler of inclusive digital transformation, DPI is essential for achieving sustainable development goals (SDGs), particularly in the health sector. Digitalization can positively contribute to the attainment of many national health goals and SDG targets by increasing the cost-effectiveness, the scope, the coverage, and the quality of many essential services. In this context, Foundational Digital Public Infrastructure (DPI-F) serves common cross-sectoral requirements, while health-specific DPI (DPI-H) provides capabilities exclusive to the health sector, which together can be designed to both amplify the potential opportunities for digitalization and mitigate the associated risks. DPI offers an alternative to the traditional siloed approach to digital development using vertical solutions, by emphasizing people-centered, interoperable digital building blocks that can simultaneously enable a variety of services and systems across public and private sectors. This strategic shift is conducive to local innovation, enabling ecosystem players to develop new services on top of the existing infrastructure – within and across sectors.

The important enabling role of DPI in sustainable development has been acknowledged in several international policy documents, and the UN has launched a High Impact Initiative on DPI to promote inclusive and open digital ecosystems for the SDGs. Both the Digital Public Good Charter and the Second Revision of the Global Digital Compact also commit to contributing to development of safe, inclusive and secure DPI. A study led by the United Nations Development Programme (UNDP)-estimates that implementation of sectoral DPIs in LMICs can accelerate GDP growth by 20-33% and enable access to some essential social services for tens of millions of people by 2030.

Alongside open standards, digital public infrastructure provides critical capabilities needed for the availability and country production of functional applications critical to health programmes across the health sector.

#### Goal

The World Health Organization (WHO) and the International Telecommunication Union (ITU) are spearheading an initiative under the Global Initiative on Digital Health (GIDH) to draw from country experiences and a growing corpus of technical guidance and country experiences, to develop guidance outlining a reference architecture for health systems that leverage DPIs and open standards to achieve health objectives. The primary goal of the development of the DPI Reference Architecture for National Digital Health Transformation is to create comprehensive guidance that encompasses a digital reference architecture, technical specifications, and implementation considerations for leveraging health-specific DPI building blocks that build on foundational cross-sectoral DPI components, to achieve health sector goals.

This approach recognizes the importance of aligning digital health platforms with local realities. The Reference Architecture guidance will be developed within the context of a new reality of constrained financing, and will need to focus on defining a reference architecture and capabilities that comprise an essential, minimal yet effective digital health base layer that any country can adopt and adapt to meet its most critical digital health needs. By emphasizing foundational capabilities—such as patient identification, core metadata registries, shared health records, standards compliant data acquisition and management, interoperability, and trusted data exchange—the guidance aims to ensure that national health systems can build to an essential suite of capabilities, providing a foundation for developing more specialized or advanced services over time.

#### Objectives

1. **Learn from Countries and Leverage Existing Guidance**: Gather, analyze and promote sharing of experiences and guidance from technical agencies, and countries that have successfully implemented health and foundational DPIs to pursue their health sector goals.
1. **Develop Normative Reference Architecture Guidance and DPI for Health Specifications**: Develop normative guidance for a standards-compliant approach to achieve up to 6 of the health sector goals (see below) using open standards, health and foundational DPI building blocks, and computable health content specifications for each of the health DPIs.

#### Digital Public Infrastructure for Health: Relevance and Requirements

The health sector is one of the main potential beneficiaries of a DPI approach. However, while the health sector's digital transformation promises significant social and economic benefits, it cannot be achieved in isolation. Cohesive digital transformation requires an integrated approach that would allow the health sector to leverage and interoperate with foundational digital solutions and systems from other sectors (e.g. registries, digital identity, payment systems). This integration empowers the health sector to harness the cross-cutting components and DPI building blocks while also seamlessly introducing solutions that address the unique needs of a person-centered healthcare delivery (i.e. health-specific DPI components).

The relevance of open standards and DPI capabilities to health has been underscored in the WHO-ITU Digital Health Platform Handbook (DHPH), in WHO SMART guidelines minimum health content packages, and the WHO/UNICEF/UNFPA/PATH Digital Implementation Investment Guide (DIIG) in 2020., The Global Initiative on Digital Health, a World Health Organization (WHO) Managed Network of Networks, launched in 2023 under the leadership of the India G20 Presidency and currently one of the priorities of the Brazil G20 Presidency also emphasizes the critical role of DPI in advancing global health outcomes.,

Despite its potential, there is insufficient investment in foundational and health-specific DPI. Many countries have been burdened by time- and resource-bound, product-based demonstration projects that do not facilitate a digital transformation of the health sector or create an enabling ecosystem for standards-based, modular digital health solutions that are extensible and sustainable. These fragmented efforts often fail to meet the varying needs of the health sector comprehensively.

The WHO-ITU DHPH highlights that a successful DPI for Health must be outcome-driven, rooted in common standards, and consider diverse stakeholder perspectives, including patients, health workers, and health systems. Quality-assured health and data content (Open Content) mapped to open interoperability standards play a fundamental role in shaping the DPI, enabling new services aligned with the SDGs. The adherence to these standards will help safeguard the integrity of the health information infrastructure, facilitate systems modularity, and make possible “build-to” specifications based on consistency in semantic and syntactic standards across the ecosystem. They ensure interoperability and information exchange among diverse applications, fostering an ecosystem where digital health solutions are inherently people-centered, inclusive, equitable, and respectful of human rights. This approach aligns seamlessly with the requirements set forth by the UN High Impact Initiative on DPI, reinforcing the importance of standardization in DPI for Health.

The DPI Reference Architecture for Digital Health Transformation will need to leverage existing best-practice frameworks, promoting a standardized approach to building health information systems that are interoperable and scalable. In particular, the Open Health Information Exchange (OpenHIE) community of practice has focused on developing an architectural framework for digital health, drawing from other work developed by the Integrating the Healthcare Enterprise (IHE). OpenHIE’s contributions are instrumental in creating a cohesive infrastructure that supports comprehensive health information exchange, crucial for achieving the health sector’s digital transformation goals.

The development of technical specifications for Digital Public Infrastructure (DPI) in health is crucial for ensuring that governments and software developers can build interoperable, scalable, and secure digital health systems to achieve sectoral health goals. For governments, clear technical specifications enable the consistent evaluation and procurement of digital solutions that align with national health goals and global standards. For software developers, these specifications provide a framework to ensure their products meet the needs of diverse health systems, fostering innovation while adhering to best practices in privacy, security, and interoperability.

This initiative focuses on learning from country experiences and developing comprehensive guidance to help countries achieve priority health goals through effective digital transformation. This project aligns with the Global Strategy on Digital Health 2020-2025, which aims to improve health for everyone, everywhere by accelerating the development and adoption of digital solutions for health.

#### WHO-ITU Flagship Programme of Work

This initiative focuses on learning from country experiences and developing comprehensive guidance to help nations achieve six priority health goals through effective digital transformation. This project aligns with the Global Strategy on Digital Health 2020-2025, which aims to improve health for everyone, everywhere by accelerating the development and adoption of digital solutions for health.

Building on the foundational work on DPI pioneered under India’s G20 Presidency, this project leverages digital solutions for public good and promotes inclusive digital transformation. The principles and frameworks established during India’s G20 Presidency are integral to the project’s approach to developing digital public infrastructure for health. The project was officially launched by WHO and ITU at the ‘GIDH Multistakeholder Dialogue on National Digital Health Transformation: Supporting Health Systems of the Future through Robust Foundations and Digital Public Infrastructure’ at the World Summit on the Information Society +20 High Level Event under the C7 eHealth Action Line in late May 2024. This launch saw participation from more than 60 countries and 152 organizations and institutions and underscored the importance of international cooperation and shared learning in achieving digital health transformation. 

#### Broader Health Goals supported by a DPI Reference Architecture Toolkit for National Digital Health Transformation

In using the proposed DPI Reference Architecture for National Digital Health Transformation, countries will be aiming to achieve broader national health system goals. These goals can include, but are not limited to:

1. Establish Trusted Personal Health Records - “every person has a right to their own health record”: Develop a secure and universally accessible system for issuing verifiable digital health records to individuals for their utilization as they seek care, following appropriate safeguards for privacy, security and consent.
1. Ensure Quality and Continuity of Care - “health workers have access to up-to-date care protocols and patient history”: Implement task-sharing and digital decision support systems to improve the continuity and quality of patient care across healthcare facilities over time to achieve integrated, person-centred care.
1. Digital Financing and Payment in Healthcare - “Informed financial planning and accountability, and protection for health system users”: Utilize digital solutions to streamline healthcare financing and strategic payment processes for improved efficiency and transparency.
1. Optimize Supply Chain Management - “no more stock outs”: Deploy digital tools for real-time monitoring and management of health product inventories to minimize stock outs and ensure timely availability.
1. Digitally-enabled Health Workforce – “Timely Pay, Proven Skills, Continuous Growth”: Ensure all health workers receive timely payments by adopting reliable digital payroll systems. This includes maintaining a health workforce registry to ensure qualification, retention, capacity building, and career development.
1. Enhance Climate Resilience with Predictive Capabilities - “The health system is dynamically responsive to evolving climate impact”: Integrate digital technologies with predictive analytics to strengthen the adaptability and proactive response of health systems against climate-related disruptions.
1. “Timely detection, assessment, reporting and action for public health risks” - Digitally Strengthen Public Health Surveillance and Response Systems, adverse event reporting, and maximize appropriate secondary use of data for public health purposes.

#### Outputs

1. DPI Reference Architecture for National Digital Health Transformation: A detailed guidance document for countries to develop and implement architected DPI and standards based national digital systems for health: that encompasses a digital reference architecture, technical specifications, and implementation considerations for leveraging health-specific DPI building blocks.
1. Health Specific DPI Specifications: Requirements and Technical specifications for each health sector specific DPI building block
1. Country Case Studies: Case studies and learning from country DPI and standards based implementations for the health sector outcome goals.



## Resource Content

```json
{
  "resourceType" : "ImplementationGuide",
  "id" : "smart.who.int.ra",
  "meta" : {
    "profile" : [
      "http://smart.who.int/base/StructureDefinition/SGImplementationGuide"
    ]
  },
  "url" : "http://smart.who.int/ra/ImplementationGuide/smart.who.int.ra",
  "version" : "0.2.0",
  "name" : "RA",
  "title" : "Reference Architecture",
  "status" : "draft",
  "experimental" : false,
  "date" : "2025-12-18T05:26:24+00:00",
  "publisher" : "WHO",
  "contact" : [
    {
      "name" : "WHO",
      "telecom" : [
        {
          "system" : "url",
          "value" : "http://who.int"
        }
      ]
    }
  ],
  "description" : "The Reference Architecture Implementation Guide to be used as a starting point for building infrastructure with the SMART Guidelines aproach",
  "jurisdiction" : [
    {
      "coding" : [
        {
          "system" : "http://unstats.un.org/unsd/methods/m49/m49.htm",
          "code" : "001",
          "display" : "World"
        }
      ]
    }
  ],
  "packageId" : "smart.who.int.ra",
  "license" : "CC-BY-SA-3.0-IGO",
  "fhirVersion" : ["4.0.1"],
  "dependsOn" : [
    {
      "id" : "hl7_terminology",
      "uri" : "http://terminology.hl7.org/ImplementationGuide/hl7.terminology",
      "packageId" : "hl7.terminology",
      "version" : "5.5.0"
    },
    {
      "id" : "hl7_fhir_uv_extensions_r4",
      "uri" : "http://hl7.org/fhir/extensions/ImplementationGuide/hl7.fhir.uv.extensions",
      "packageId" : "hl7.fhir.uv.extensions.r4",
      "version" : "5.1.0"
    },
    {
      "id" : "hl7_fhir_uv_cql",
      "uri" : "http://hl7.org/fhir/uv/cql/ImplementationGuide/hl7.fhir.uv.cql",
      "packageId" : "hl7.fhir.uv.cql",
      "version" : "1.0.0"
    },
    {
      "id" : "hl7_fhir_uv_crmi",
      "uri" : "http://hl7.org/fhir/uv/crmi/ImplementationGuide/hl7.fhir.uv.crmi",
      "packageId" : "hl7.fhir.uv.crmi",
      "version" : "1.0.0"
    },
    {
      "id" : "hl7_fhir_uv_sdc",
      "uri" : "http://hl7.org/fhir/uv/sdc/ImplementationGuide/hl7.fhir.uv.sdc",
      "packageId" : "hl7.fhir.uv.sdc",
      "version" : "3.0.0"
    },
    {
      "id" : "hl7_fhir_uv_cpg",
      "uri" : "http://hl7.org/fhir/uv/cpg/ImplementationGuide/hl7.fhir.uv.cpg",
      "packageId" : "hl7.fhir.uv.cpg",
      "version" : "2.0.0"
    },
    {
      "id" : "hl7_fhir_us_cqfmeasures",
      "uri" : "http://hl7.org/fhir/us/cqfmeasures/ImplementationGuide/hl7.fhir.us.cqfmeasures",
      "packageId" : "hl7.fhir.us.cqfmeasures",
      "version" : "5.0.0"
    },
    {
      "id" : "hl7_fhir_uv_extensions_r5",
      "uri" : "http://hl7.org/fhir/extensions/ImplementationGuide/hl7.fhir.uv.extensions",
      "packageId" : "hl7.fhir.uv.extensions.r5",
      "version" : "5.2.0"
    },
    {
      "id" : "IHE_ITI_mCSD",
      "uri" : "https://profiles.ihe.net/ITI/mCSD/ImplementationGuide/ihe.iti.mcsd",
      "packageId" : "ihe.iti.mcsd",
      "version" : "4.0.0"
    },
    {
      "id" : "IHE_ITI_SVCM",
      "uri" : "https://profiles.ihe.net/ITI/mCSD/ImplementationGuide/ihe.iti.svcm",
      "packageId" : "ihe.iti.svcm",
      "version" : "1.5.1"
    },
    {
      "id" : "pcmt",
      "extension" : [
        {
          "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ImplementationGuide.dependsOn.reason",
          "valueMarkdown" : "This IG uses SMART base computable guideline capabilities"
        }
      ],
      "uri" : "http://smart.who.int/pcmt/ImplementationGuide/smart.who.int.pcmt",
      "packageId" : "smart.who.int.pcmt",
      "version" : "0.1.0"
    },
    {
      "id" : "sb",
      "extension" : [
        {
          "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ImplementationGuide.dependsOn.reason",
          "valueMarkdown" : "This IG uses SMART base computable guideline capabilities"
        }
      ],
      "uri" : "http://smart.who.int/base/ImplementationGuide/smart.who.int.base",
      "packageId" : "smart.who.int.base",
      "version" : "0.1.0"
    }
  ],
  "definition" : {
    "extension" : [
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "copyrightyear"
          },
          {
            "url" : "value",
            "valueString" : "2023+"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "releaselabel"
          },
          {
            "url" : "value",
            "valueString" : "ci-build"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "autoload-resources"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "path-liquid"
          },
          {
            "url" : "value",
            "valueString" : "template/liquid"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "path-liquid"
          },
          {
            "url" : "value",
            "valueString" : "input/liquid"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "path-qa"
          },
          {
            "url" : "value",
            "valueString" : "temp/qa"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "path-temp"
          },
          {
            "url" : "value",
            "valueString" : "temp/pages"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "path-output"
          },
          {
            "url" : "value",
            "valueString" : "output"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "path-suppressed-warnings"
          },
          {
            "url" : "value",
            "valueString" : "input/ignoreWarnings.txt"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "path-history"
          },
          {
            "url" : "value",
            "valueString" : "http://smart.who.int/ra/history.html"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "template-html"
          },
          {
            "url" : "value",
            "valueString" : "template-page.html"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "template-md"
          },
          {
            "url" : "value",
            "valueString" : "template-page-md.html"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "apply-contact"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "apply-context"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "apply-copyright"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "apply-jurisdiction"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "apply-license"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "apply-publisher"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "apply-version"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "apply-wg"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "active-tables"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "fmm-definition"
          },
          {
            "url" : "value",
            "valueString" : "http://hl7.org/fhir/versions.html#maturity"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "propagate-status"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "excludelogbinaryformat"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "tabbed-snapshots"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-internal-dependency",
        "valueCode" : "hl7.fhir.uv.tools.r4#0.9.0"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "copyrightyear"
          },
          {
            "url" : "value",
            "valueString" : "2023+"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "releaselabel"
          },
          {
            "url" : "value",
            "valueString" : "ci-build"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "autoload-resources"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "path-liquid"
          },
          {
            "url" : "value",
            "valueString" : "template/liquid"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "path-liquid"
          },
          {
            "url" : "value",
            "valueString" : "input/liquid"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "path-qa"
          },
          {
            "url" : "value",
            "valueString" : "temp/qa"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "path-temp"
          },
          {
            "url" : "value",
            "valueString" : "temp/pages"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "path-output"
          },
          {
            "url" : "value",
            "valueString" : "output"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "path-suppressed-warnings"
          },
          {
            "url" : "value",
            "valueString" : "input/ignoreWarnings.txt"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "path-history"
          },
          {
            "url" : "value",
            "valueString" : "http://smart.who.int/ra/history.html"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "template-html"
          },
          {
            "url" : "value",
            "valueString" : "template-page.html"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "template-md"
          },
          {
            "url" : "value",
            "valueString" : "template-page-md.html"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "apply-contact"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "apply-context"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "apply-copyright"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "apply-jurisdiction"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "apply-license"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "apply-publisher"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "apply-version"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "apply-wg"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "active-tables"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "fmm-definition"
          },
          {
            "url" : "value",
            "valueString" : "http://hl7.org/fhir/versions.html#maturity"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "propagate-status"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "excludelogbinaryformat"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "tabbed-snapshots"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      }
    ],
    "resource" : [
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "ActorDefinition"
          }
        ],
        "reference" : {
          "reference" : "ActorDefinition/ClientRegistry"
        },
        "name" : "Client Registry",
        "description" : "The Client Registry assists in uniquely identifying individuals who receive health care services by:\r\nMaintaining a central registry of all patients and their demographics and assigning a unique identifier to each patient.  \n\r\nLinking patient registration entries that result due to changes in patient demographics (patient moved to another location), data entry errors during patient registration, or missing demographic information.  \n\r\nEnabling health care workers to identify facilities at which a patient has received care.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "ActorDefinition"
          }
        ],
        "reference" : {
          "reference" : "ActorDefinition/FacilityRegistry"
        },
        "name" : "Facility Registry",
        "description" : "A registry that stores and manages standardized information about health facilities, serving as a central authority for facility data.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "ActorDefinition"
          }
        ],
        "reference" : {
          "reference" : "ActorDefinition/HealthManagementInformationSystem"
        },
        "name" : "Health Management Information System",
        "description" : "A system that collects, analyzes, and reports health data for monitoring and decision-making purposes.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "ActorDefinition"
          }
        ],
        "reference" : {
          "reference" : "ActorDefinition/HealthWorkerRegistry"
        },
        "name" : "Health Worker Registry",
        "description" : "A registry that maintains information about health workers, including their identifiers, roles, and affiliations.  \n\r\nThe Health Worker Registry serves as an authority for maintaining the unique identities of health workers within a context.  \n\r\n* Pulls the minimum dataset of health workforce information from the various source data systems.  \n \r\n* Merges the source data systems into an authoritative registry of health workers according to a data governance policy.   \n\r\n* Allows queries of health worker information by client systems.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "ActorDefinition"
          }
        ],
        "reference" : {
          "reference" : "ActorDefinition/InteroperabilityLayer"
        },
        "name" : "Interoperability Layer",
        "description" : "A component that enables communication of services across domains and organizations, This MMAY include:  \n - Service discovery and identification  \n - Service identity life cycle management  \n - Encryption of service to service communications  \n - Authentication, authorization and permissions at the service level (not application or user level)  \n - Service monitoring and transaction logging  \n\nDepending on the governance requirements, this layer may also include tools to centralize service logic including message routing, workflow and service orchestration, and message translation.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "ActorDefinition"
          }
        ],
        "reference" : {
          "reference" : "ActorDefinition/LogisticsManagementInformationSystem"
        },
        "name" : "Logistics Management Information System",
        "description" : "A system that manages the supply chain operations, including tracking and distribution of health commodities.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "ActorDefinition"
          }
        ],
        "reference" : {
          "reference" : "ActorDefinition/PointOfServiceSystem"
        },
        "name" : "Point-of-Service System",
        "description" : "A system used at the point of care, such as electronic medical records (EMRs), to capture and manage patient encounters and clinical data.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "ActorDefinition"
          }
        ],
        "reference" : {
          "reference" : "ActorDefinition/SharedHealthRecord"
        },
        "name" : "Shared Health Record",
        "description" : "A centralized repository that stores and manages longitudinal patient health records, enabling access to clinical data across systems.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "ActorDefinition"
          }
        ],
        "reference" : {
          "reference" : "ActorDefinition/TerminologyService"
        },
        "name" : "Terminology Service",
        "description" : "A service that provides access to standardized code systems, value sets, and mappings to ensure consistent use of terminology across systems.",
        "exampleBoolean" : false
      }
    ],
    "page" : {
      "extension" : [
        {
          "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
          "valueUrl" : "toc.html"
        }
      ],
      "nameUrl" : "toc.html",
      "title" : "Table of Contents",
      "generation" : "html",
      "page" : [
        {
          "extension" : [
            {
              "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
              "valueUrl" : "index.html"
            }
          ],
          "nameUrl" : "index.html",
          "title" : "Home",
          "generation" : "markdown",
          "page" : [
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "changes.html"
                }
              ],
              "nameUrl" : "changes.html",
              "title" : "Changes",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "dependencies.html"
                }
              ],
              "nameUrl" : "dependencies.html",
              "title" : "Dependencies",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "references.html"
                }
              ],
              "nameUrl" : "references.html",
              "title" : "References",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "adapting.html"
                }
              ],
              "nameUrl" : "adapting.html",
              "title" : "Adapting Guidelines for Country use",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "license.html"
                }
              ],
              "nameUrl" : "license.html",
              "title" : "License",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "governance.html"
                }
              ],
              "nameUrl" : "governance.html",
              "title" : "Governance and Operational Framework for the DPI-H Reference Architecture Technical Working Group (TWG)",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "architects_guide.html"
                }
              ],
              "nameUrl" : "architects_guide.html",
              "title" : "Architect's Guide",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "scoping.html"
                }
              ],
              "nameUrl" : "scoping.html",
              "title" : "Scoping",
              "generation" : "markdown"
            }
          ]
        },
        {
          "extension" : [
            {
              "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
              "valueUrl" : "business-requirements.html"
            }
          ],
          "nameUrl" : "business-requirements.html",
          "title" : "Business Requirements",
          "generation" : "markdown",
          "page" : [
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "concepts.html"
                }
              ],
              "nameUrl" : "concepts.html",
              "title" : "Concepts",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "personas.html"
                }
              ],
              "nameUrl" : "personas.html",
              "title" : "Generic Personas",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "scenarios.html"
                }
              ],
              "nameUrl" : "scenarios.html",
              "title" : "User Scenarios",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "business-processes.html"
                }
              ],
              "nameUrl" : "business-processes.html",
              "title" : "Business Processes",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "dictionary.html"
                }
              ],
              "nameUrl" : "dictionary.html",
              "title" : "Data Dictionary",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "decision-logic.html"
                }
              ],
              "nameUrl" : "decision-logic.html",
              "title" : "Decision-support logic",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "indicators.html"
                }
              ],
              "nameUrl" : "indicators.html",
              "title" : "Indicator and Performance Metrics",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "functional-requirements.html"
                }
              ],
              "nameUrl" : "functional-requirements.html",
              "title" : "Functional Requirements",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "non-functional-requirements.html"
                }
              ],
              "nameUrl" : "non-functional-requirements.html",
              "title" : "Non-functional Requirements",
              "generation" : "markdown"
            }
          ]
        },
        {
          "extension" : [
            {
              "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
              "valueUrl" : "data-models-and-exchange.html"
            }
          ],
          "nameUrl" : "data-models-and-exchange.html",
          "title" : "Data Models and Exchange",
          "generation" : "markdown",
          "page" : [
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "system-actors.html"
                }
              ],
              "nameUrl" : "system-actors.html",
              "title" : "System Actors",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "sequence-diagrams.html"
                }
              ],
              "nameUrl" : "sequence-diagrams.html",
              "title" : "Sequence Diagrams",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "transactions.html"
                }
              ],
              "nameUrl" : "transactions.html",
              "title" : "Transactions",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "indicators-measures.html"
                }
              ],
              "nameUrl" : "indicators-measures.html",
              "title" : "Indicators and Measures",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "codings.html"
                }
              ],
              "nameUrl" : "codings.html",
              "title" : "Codings",
              "generation" : "markdown"
            }
          ]
        },
        {
          "extension" : [
            {
              "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
              "valueUrl" : "deployment.html"
            }
          ],
          "nameUrl" : "deployment.html",
          "title" : "Deployment",
          "generation" : "markdown",
          "page" : [
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "security-privacy.html"
                }
              ],
              "nameUrl" : "security-privacy.html",
              "title" : "Security and Privacy Considerations",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "testing.html"
                }
              ],
              "nameUrl" : "testing.html",
              "title" : "Testing",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "test-data.html"
                }
              ],
              "nameUrl" : "test-data.html",
              "title" : "Test Data",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "reference-implementations.html"
                }
              ],
              "nameUrl" : "reference-implementations.html",
              "title" : "Reference Implementations",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "trust_domain.html"
                }
              ],
              "nameUrl" : "trust_domain.html",
              "title" : "Trust Domains",
              "generation" : "markdown"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "downloads.html"
                }
              ],
              "nameUrl" : "downloads.html",
              "title" : "Downloads",
              "generation" : "markdown"
            }
          ]
        },
        {
          "extension" : [
            {
              "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
              "valueUrl" : "indices.html"
            }
          ],
          "nameUrl" : "indices.html",
          "title" : "Indices",
          "generation" : "markdown",
          "page" : [
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "artifacts.html"
                }
              ],
              "nameUrl" : "artifacts.html",
              "title" : "Artifact Index",
              "generation" : "html"
            },
            {
              "extension" : [
                {
                  "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
                  "valueUrl" : "maps.html"
                }
              ],
              "nameUrl" : "maps.html",
              "title" : "Mappings",
              "generation" : "markdown"
            }
          ]
        },
        {
          "extension" : [
            {
              "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
              "valueUrl" : "dak-api.html"
            }
          ],
          "nameUrl" : "dak-api.html",
          "title" : "DAK API Documentation Hub",
          "generation" : "markdown"
        }
      ]
    },
    "parameter" : [
      {
        "code" : "path-resource",
        "value" : "input/capabilities"
      },
      {
        "code" : "path-resource",
        "value" : "input/examples"
      },
      {
        "code" : "path-resource",
        "value" : "input/extensions"
      },
      {
        "code" : "path-resource",
        "value" : "input/models"
      },
      {
        "code" : "path-resource",
        "value" : "input/operations"
      },
      {
        "code" : "path-resource",
        "value" : "input/profiles"
      },
      {
        "code" : "path-resource",
        "value" : "input/resources"
      },
      {
        "code" : "path-resource",
        "value" : "input/vocabulary"
      },
      {
        "code" : "path-resource",
        "value" : "input/maps"
      },
      {
        "code" : "path-resource",
        "value" : "input/testing"
      },
      {
        "code" : "path-resource",
        "value" : "input/history"
      },
      {
        "code" : "path-resource",
        "value" : "fsh-generated/resources"
      },
      {
        "code" : "path-pages",
        "value" : "template/config"
      },
      {
        "code" : "path-pages",
        "value" : "input/images"
      },
      {
        "code" : "path-tx-cache",
        "value" : "input-cache/txcache"
      }
    ]
  }
}

```
