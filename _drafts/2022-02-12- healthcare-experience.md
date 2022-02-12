---
layout: post
title: "Healthcare Experience"
date: 2022-02-12 12:00:00 +0200
categories: portfolio repository golang fhir
---

![Waterloo Tree Inventory](https://www.hildeberto.com/roma/images/waterloo_tree_inventory.png)

I'm over a year working in the healthcare industry. Before that, I was involded in education and finance, two industries before with significant impact on people's life. But the impact of healthcare is far more important because you may be poor or poorly educated, but being poorly healthy is a life threatening situation. Also, a bug in an education system is upsetting, but it can be fixed without major impact. A bug in a financial system is troublesome to many people involved but they all have a chance to recover with the help of the government and ensurance companies. In a healthcare system, a bug can kill people. Loosing a simple allergy reaction record can represent severe complications during a surgery.

<!-- more -->

There is no shortage of complex problems to solve in healthcare and they are pushing me to become a better engineer. I was recently introduced to a popular standard called [HL7&reg; FHIR&reg;](https://hl7.org/fhir/), which has been used not only to integrate heterogeneous systems, but also to enable a marketplace of applications that exponentially expands the offering of services and solutions for patients and care givers. FHIR&reg; is for healthcare what [Swift](https://www.swift.com/standards/iso-20022) is for finance.

FHIR&reg; (Fast Healthcare Interoperability Resources) - pronunced like "fire" - structures healthcare data in resources, which are composed of elements, which are strongly typed. From that you get that resources follow the object-oriented paradigm in the way Java and C# implement it. They use abstractions similar to classes, attributes, methods, and enheritance. Resources are serialized in multiple formats, but the most frequent are JSON and XML. Transfering serialized resources over the web also pushed the standard to follow REST principles, using Restful APIs as the main method of interoperability. The most powerful characteristic of the standard is its extensibility. New resources can be created, existing resources and elements can be extended, new elements can be added, all that while still compliant with the standard.

The "F" in the acronym FHIR stands for "Fast". It is not clear what they mean by that, but it seems to be related to productivity, given the experiences they report of people producing and consuming resources within a day. Let's not be fooled by that because FHIR is complex and the only way to be productive is using one of the available libraries. The most commonly used are in Java, C#, and JavaScript. They are high level languages that match all abstractions required by the standard.

In any case, I'm pretty sure that "Fast" is not about runtime performance. It depends on the library and the design of the system. My concern about those libraries is that, even though they are performant, they consume a large amount of computing resources, making solutions expensive to serve.