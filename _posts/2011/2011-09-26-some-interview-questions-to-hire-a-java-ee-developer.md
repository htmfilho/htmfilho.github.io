---
layout: post
title: "Some Interview Questions to Hire a Java EE Developer"
date: 2011-09-26 10:24:00 +0200
categories: career enterprise application java software architecture software engineering web services
---

The Internet is full of interview questions for Java developers. The main problem of those questions is that they only prove that the candidate has a good memory, remmembering all that syntax, structures, constants, etc. There is not real evaluation of his/her logical reasoning.

I’m listing bellow some examples of interview questions that check the knowledge of the candidate based on his/her experience. The questions were formulated to verify whether the candidate is capable of fulfilling the role of a Java enterprise applications developer. I’m also putting the anwsers in case anybody want to discuss the questions.

**1. Can you give some examples of improvements in the Java EE5/6 specification in comparison to the J2EE specification?**

The new specification favours convention over configuration and introduces annotations to replace the use of XML for configuration. Inheritance is not used to define components anymore. They are defined, instead, as POJOs. To empower those POJOs with enterprise features, dependency injection was put in place, simplifying the use of EJBs. The persistence layer was fully replaced by the Java Persistence API (JPA).

**2. Considering two enterprise systems developed in different platforms, which good options do you propose to exchange data between them?**

We can see as potential options nowadays the use of web services and message queues, depending on the scenario. For example: when a system needs to send data, as soon as they are available, to another system or make data available for several systems, then a message queuing system is recommended. When a system has data to be processed by another system and needs back the result of this processing synchronously, then web service is the most indicated option.

**3. What do you suggest to implement asynchronous code in Java EE?**

There are several options: one can post messages to a queue to be consumed by a Message-Driven Bean (MDB); or annotate a method with @Timer to define the time to execute the code programmatically; or annotate a method with @Scheduler to define the time to execute the code declaratively.

**4. Can you illustrate the use of Stateless Session Bean, Statefull Session Bean and Singleton Session Bean?**

Stateless Session Beans are used when there is no need to preserve the state of objects between several business transactions. Every transaction has its own instances and instances of components can be retrieved from pools of objects. It is recommended for most cases, when several operations are performed within a transaction to keep the database consistency.

Statefull Session Beans are used when there is the need to preserve the state of objects between business transactions. Every instance of the component has its own objects. These objects are modified by different transactions and they are discarded after reaching a predefined time of inactivity. They can be used to cache those data with intensive use, such as reference data and long record sets for pagination, in order to reduce the volume of IO operations with the database.

A singleton session bean is instantiated once per application and exists for the lifecycle of the application. Singleton session beans are designed for circumstances in which a single enterprise bean instance is shared across and concurrently accessed by clients. They maintain their state between client invocations, which requires a careful implementation to avoid conflicts when accessed concurrently. This kind of component can be used, for example, to initialize the application at its start-up and share a specific object across the application.

**5. What is the difference between queue and topic in a message queuing system?**

In a queue there is only one producer of messages and only one consumer of these messages (1 – 1). In a topic there is a publisher of messages and several subscribers that will receive those messages (1 – N).

**6. Which strategies do you consider to import and export XML content?**

If the XML document is formally defined in a schema, we can use JAXB to serialize and deserialize objects into/from XML according to the schema. If the XML document does not have a schema, then there are two situations: 1) when the whole XML content should be consider: In this case, serial access to the whole document is recommended using SAX, or accessed randomly using DOM; 2) when only parts of the XML content should be considered, than XPath can be used or StAX in case operations should be executed immediately after each desired part is found in the document.

**7. Can you list some differences between a relational model and an object model?**

An object model can be mapped to a relational model, but there are some differences that should be taken into consideration. In the relational model a foreign key has the same type of the target’s primary key, but in the object model and attribute points to the entire related object. In the object model it is possible to have N-N relationships while in the relational model an intermediary entity is needed. There is no support for inheritance, interface, and polymorphism in the relational model.

**8. What is the difference between XML Schema, XSLT, WSDL and SOAP?**

A XML Schema describes the structure of an XML document and it is used to validate these documents. WSDL (Web Service Definition Language) describes the interface of SOAP-based web services. It can refer to XML schemas to define existing complex types passed by parameter or returned to the caller. SOAP (Simple Object Access Protocol) is the format of the message used to exchange data in a web service call. XSLT (eXtensible Stylesheet Language Transformation) is used to transform XML documents into other document formats.

**9. How would you configure an environment to maximize productivity of a development team?**

Every developer should have a personal environment capable of executing the whole application in his/her local workstation. The project should be synchronized between developers using a version control system. Integration routines must be executed periodically in order to verify the compatibility and communication between all components of the system. Unit and integration tests must be executed frequently.<br/>—

You can increment this set of questions covering other subjects like unit testing, dependence injection,  version control and so on. Try to formulate the questions in a way that you don’t get a single answer, but a short analysis from the candidate. People can easily find answers on the Internet, but good analysis can be provided only with accumulated experience.
