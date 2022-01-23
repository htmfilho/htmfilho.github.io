---
layout: post
title: "New CEJUG Open Source Project"
date: 2011-01-02 11:29:00 +0200
categories: cejug enterprise application integration java netbeans open source security software architecture web
---

I’m working on a new project, managed by the [CEJUG](http://www.cejug.org/) community, which aims to develop a web application for managing Java User Groups. We put it into [production](http://www.cejug.org/jug) in the first day of the decade, January 1st, 2011, and we made the [source code freely available](http://java.net/projects/cejug/sources/svn/show/trunk/jug) on our [java.net project](http://www.java.net/projects/cejug).

The first goal we want to achieve is the definition of what is actually being a CEJUG member. Nowadays, we simply consider all those registered in our technical mailing as members. This simplicity is good for management purposes, but we lose lots of information because of that. We don’t know, for instance, for what reasons a member is leaving the group. Did we do something wrong? What can we do to get better and get members back into the boat? We also noticed that even non-technical people, as entrepreneurs, recruiters, and those  who decided to unsubscribe because of too many messages, would like to keep in touch with the group, not necessarily going into technical discussions, but proposing other ways to help. Adopting a separate application to manage subscriptions would help us to collect more feedback and be more inclusive.

Developing our own solution can make data work in our favour and allow our sustained growth. Consequently, we are generating an additional source of knowledge for the community. This  application is open source and everyone can run and see how CEJUG works. Beginners will have a solid source to start their studies on the development of Java web applications, experts  can help with bug fixing, refactoring, and developing new features  according to our [issue tracking](http://java.net/jira/browse/CEJUG). Adopted design patterns may be subject of valuable and warming discussions in our community.

![cejug-application-300x153.png](/images/posts/cejug-application-300x153.png)

Of course the application was developed in Java 😉 We have the duty to write the software architecture document in the coming days, but we can already say in advance what we are using to develop and deploy the application. The presentation layer was developed in [JSF 2.0](http://jcp.org/en/jsr/detail?id=314), using the [Primefaces](http://www.primefaces.org/) component library; the business layer was implemented in [EJB 3.1](http://jcp.org/en/jsr/detail?id=318); the persistence layer was implemented in [JPA 2.0](http://jcp.org/en/jsr/detail?id=317); data is persisted in [MySQL](http://www.mysql.com/); and everything is running on [Glassfish 3.0.1](http://glassfish.java.net/) Application Server. The current version was developed using [Netbeans 6.9](http://www.netbeans.org/) due to its productivity when developing JEE applications. We rely on the container to manage security, database transactions, connection pools, and email sessions.

The next step is to document the application, add customisable features and internationalise it in order to spread its adoption by several other JUGs out there. We are looking for contributors and supporters to make this a successful open source project. We hope one day, we could promote interoperability between JUGs through this application, sharing mutual knowledge, events, effort on the growth of the Java platform and the Java community.
