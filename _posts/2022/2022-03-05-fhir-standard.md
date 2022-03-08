---
layout: post
title: "FHIR: A Standard For Healthcare Data Interoperability"
date: 2022-02-12 12:00:00 +0200
image: /images/posts/dragon-sketch.png
categories: fhir healthcare api standard
---

![Sketching a Dragon](/images/posts/dragon-sketch.png)

I'm over a year working in the healthcare industry. Before that, I was involded in education and finance. These are industries with significant impact on people's lives, but the impact of healthcare is far more important because we may be poor or poorly educated, but being poorly healthy is a life threatening situation. A bug in an education system is upsetting, but it can be fixed without major impact. A bug in a financial system is troublesome to many people but they all have a chance to recover with the help of government and ensurance companies. In a healthcare system, a bug can kill people. Loosing a simple allergy reaction record can represent severe complications during a surgery, for example.

<!-- more -->

There is no shortage of complex problems to solve in healthcare and they are pushing me to become a better engineer. While working at [PointClickCare](https://www.pointclickcare.com), I was exposed to a popular standard called [HL7&reg; FHIR&reg;](https://hl7.org/fhir/), which has been used not only to integrate heterogeneous systems, but also to enable a marketplace of applications that exponentially expands the offering of services for patients and care givers.

FHIR&reg; (Fast Healthcare Interoperability Resources) is for healthcare what [Swift](https://www.swift.com/standards/iso-20022) is for finance. It is not simple. It takes some time to diggest but it seems to have just enough complexity to cover the needs of healthcare without limiting systems and users. What I don't get is the meaning of the word "Fast" in the acronym. I'm pretty sure it's not about runtime performance. It depends on the library and the design of the system. I think it's probably about productivity because there is a mature ecosystem out there to build solutions within hours, under the most optimistic circumstances of course.

FHIR&reg; - pronounced like "fire" - structures healthcare data into resources, which also match the concept of _resource_ in **REST** (RepResourceresentational State Transfer), making it an excellent standard to build healthcare APIs. Resources are composed of strongly typed elements. From that, we get that resources also follow the object-oriented paradigm in the way Java and C# implement it. They use abstractions similar to classes, attributes, methods, and inheritance. Resources are serialized in multiple formats such as JSON, XML, and RDF. The most powerful characteristic of the standard is **extensibility**. New resources can be created - by extending the [Basic](https://hl7.org/fhir/basic.html) resource -, existing resources and elements can be extended, new elements can be added, all that while still compliant with the standard and without breaking interoperability. Here is how a [Patient](http://hl7.org/fhir/patient.html) resource looks like in JSON format:

{% highlight json %}
{
  "resourceType": "Patient",
  "id": "8973647",
  "text": {
    "status": "generated",
    "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: f001</p><p><b>identifier</b>: 738472983 (USUAL), ?? (USUAL)</p><p><b>active</b>: true</p><p><b>name</b>: Pieter van de Heuvel </p><p><b>telecom</b>: ph: 0648352638(MOBILE), p.heuvel@gmail.com(HOME)</p><p><b>gender</b>: male</p><p><b>birthDate</b>: 17/11/1944</p><p><b>deceased</b>: false</p><p><b>address</b>: Van Egmondkade 23 Amsterdam 1024 RJ NLD (HOME)</p><p><b>managingOrganization</b>: <a>Burgers University Medical Centre</a></p></div>"
  },
  "identifier": [
    {
      "use": "usual",
      "system": "urn:oid:2.16.840.1.113883.2.4.6.3",
      "value": "738472983"
    }
  ],
  "active": true,
  "name": [
    {
      "use": "usual",
      "family": "van de Heuvel",
      "given": [
        "Pieter"
      ],
      "suffix": [
        "MSc"
      ]
    }
  ],
  "telecom": [
    {
      "system": "phone",
      "value": "0648352638",
      "use": "mobile"
    },
    {
      "system": "email",
      "value": "p.heuvel@gmail.com",
      "use": "home"
    }
  ],
  "gender": "male",
  "birthDate": "1944-11-17",
  "deceasedBoolean": false,
  "address": [
    {
      "use": "home",
      "line": [
        "Van Egmondkade 23"
      ],
      "city": "Amsterdam",
      "postalCode": "1024 RJ",
      "country": "NLD"
    }
  ],
  "maritalStatus": {
    "coding": [
      {
        "system": "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus",
        "code": "M",
        "display": "Married"
      }
    ],
    "text": "Getrouwd"
  },
  "managingOrganization": {
    "reference": "Organization/f001",
    "display": "Burgers University Medical Centre"
  }
}
{% endhighlight %}

But the Patient resource does not contain anything about the health of a patient. For that, we need other resources like [Condition](http://hl7.org/fhir/condition.html) and [Observation](http://hl7.org/fhir/observation.html). The Condition below indicates that the Patient above has a mild form of asthma. Notice the reference to the Patient in the attribute "subject":

{% highlight json %}
{
  "resourceType": "Condition",
  "id": "example2",
  "text": {
    "status": "generated",
    "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">Mild Asthma</div>"
  },
  "clinicalStatus": {
    "coding": [
      {
        "system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
        "code": "active"
      }
    ]
  },
  "verificationStatus": {
    "coding": [
      {
        "system": "http://terminology.hl7.org/CodeSystem/condition-ver-status",
        "code": "confirmed"
      }
    ]
  },
  "category": [
    {
      "coding": [
        {
          "system": "http://terminology.hl7.org/CodeSystem/condition-category",
          "code": "problem-list-item",
          "display": "Problem List Item"
        }
      ]
    }
  ],
  "severity": {
    "coding": [
      {
        "system": "http://snomed.info/sct",
        "code": "255604002",
        "display": "Mild"
      }
    ]
  },
  "code": {
    "text": "Asthma"
  },
  "subject": {
    "reference": "Patient/8973647"
  }
}
{% endhighlight %}

[Many other resources](https://hl7.org/fhir/resourcelist.html) are available to exchange healthcare data, but we don't have to build anything from scratch to deal with those resources. There are many FHIR&reg; implementations out there and one will probably match your stack, saving a ton amount of work. The most commonly used are [Hapi FHIR](https://hapifhir.io/) (Java), [Firely .NET](https://fire.ly/products/firely-net-sdk/) (C#), and [fhir.js](https://github.com/FHIR/fhir.js/) (JavaScript). They are high level languages that match all abstractions required by the standard. Here are some advantages of using these libraries:

1. A single client implementation can connect and exchange data with multiple compliant servers.

2. We don't have to build an in-house FHIR&reg; client because one probably exists for our stack, giving us data ready to be processed.

3. If more data needs to be exchanged out of what FHIR&reg; already offers, then the extension framework can be used to serve the data without breaking compatibility with existing clients.

Some active members of the community make FHIR&reg; servers openly available for learning purpose. Hapi FHIR is one of those. Visit http://hapi.fhir.org/ to explore generated fake resources. We can even call the endpoints, as documented in the [Swagger](http://hapi.fhir.org/baseR4/swagger-ui/) page:

    $ curl --location --request GET 'http://hapi.fhir.org/baseR4/Patient/1963546'

This call returns the following response:

{% highlight json %}
{
  "resourceType": "Patient",
  "id": "1963546",
  "meta": {
    "versionId": "1",
    "lastUpdated": "2021-03-23T05:30:45.180+00:00",
    "source": "#07OvOvGcTSCrnZYI"
  },
  "text": {
    "status": "generated",
    "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><div class=\"hapiHeaderText\">Bob <b>ALEXANDER </b></div><table class=\"hapiPropertyTable\"><tbody><tr><td>Identifier</td><td>4f524274-0aca-4246-b20c-6d73e9862beb</td></tr></tbody></table></div>"
  },
  "identifier": [
    {
      "type": {
        "coding": [
          {
            "system": "http://hl7.org/fhir/v2/0203",
            "code": "MR"
          }
        ]
      },
      "value": "4f524274-0aca-4246-b20c-6d73e9862beb"
    }
  ],
  "name": [
    {
      "family": "Alexander",
      "given": [
        "Bob"
      ]
    }
  ]
}
{% endhighlight %}

In addition to building APIs, FHIR&reg; can be used to define messages to post in messaging systems such as [RabbitMQ](https://www.rabbitmq.com) and [Kafka](https://kafka.apache.org). It can also be used to create documents that represent all records of a patient or an entire organization, with the intent of archiving or transferring large volumes of data. I can go on and on, listing everything that can be done with FHIR&reg;, but this is a blog post, not a book. But, that's probably a subject that I'm going to explore further, to help with its dissemination and perhaps to inspire other industries to take similar initiatives.

<hr>

_* HL7 and FHIR are the registered trademarks of Health Level Seven International and their use does not constitute endorsement by HL7_.