---
layout: post
title: "Healthcare Experience"
date: 2022-02-12 12:00:00 +0200
categories: portfolio repository golang fhir
---

![Waterloo Tree Inventory](https://www.hildeberto.com/roma/images/waterloo_tree_inventory.png)

I'm over a year working in the healthcare industry. I've worked in the education and financial industries before. They both impacts people's life, but the impact of healthcare is far more important because you may be poor or poorly educated, but we are in trouble when we are poorly healthy. Also, a bug in an education application is just annoying  and can be easily fixed. A bug in a financial software can make many people upset but they all have a chance to recover. While in a healthcare application, a bug can kill people. Loosing a simple allergy reaction record can represent severe complications during a surgery. The criticality and complexity of healthcare systems pushed me to become a better engineer.

<!-- more -->

It turns out, there is no shortage of complex problems to solve in healthcare. Solving them is deeply exciting. I was recently introduced to a popular standard called HL7 FHIR V4, which has been used not only to integrate heterogeneous systems, but also to enable a marketplace of applications that exponentially expands the offering of services and solutions. I'm surprised that other industries don't have anything close to what the healthcare industry achieved with this standard. The closest I found is the Swift standard for international money transactions.


FHIR (pronunced like fire) structures health data in resources, which are composed of elements, which are strongly typed. From that you get that resources follow the object-oriented paradigm in the way that Java and C# implement it, using abstractions similar to classes, attributes, methods, and enheritance. Resources are serialized in multiple formats, but the most frequent are JSON and XML. Transfering serialized resources over the web also pushed the standard to follow REST principles, using Restful APIs as the main method of interoperability. The most powerful characteristic of the standard is the extensibility. New resources can be created, existing resources can be extended, new elements can be added and existing elements can be extended, all those while still compliant with the standard.

The "F" in the acronym FHIR stands for "Fast". It is not clear what they mean by that, but it seems to be related to productivity, given the experiences they report of people producing and consuming resources within a day. I'm pretty sure it doesn't mean runtime performance though, because it really depends on the implementation and, compared to other standards, FHIR certainly uses more network bandwidth. The most commonly used implementations are in Java, C#, and JavaScript. They are high level languages that match all abstractions required by the standard. So, they are natural choices to develop backend and frontend healthcare systems and our best chance of productivity at this point in time.