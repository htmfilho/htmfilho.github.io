---
layout: post
title: "What is a Middleware? A Platform, A Framework or What?"
date: 2009-05-26 18:59:00 +0200
categories: enterprise application integration java operating system software architecture
---

Some time ago I wrote a post about <a href="http://www.hildeberto.com/2008/10/platform-versus-framework.html">the difference between “platform” and “framework”</a> and recently a reader, <a href="http://www.blogger.com/profile/17997742353906252825">Hemanth Gowda</a>,  posted a comment to that text, asking how the concept of “<a href="http://en.wikipedia.org/wiki/Middleware">middleware</a>” is positioned among those definitions.

In my opinion, the concept of middleware is all about service providing. While a platform allows a software to run and a framework is more focused on software design, a middleware will provide services for your application. These services will allow your application to support many concurrent users, connect to several data sources, interoperate with services provided by other middleware instances, expand the platform to scale the application, support several frameworks to give flexibility for developers and many other relevant features.

The best example of middleware in the Java world is an application server, such as <a href="https://glassfish.dev.java.net/">Glassfish</a>, <a href="http://www.jboss.org/">JBoss</a> and <a href="http://www.blogger.com/www.ibm.com/websphere/">Websphere</a>. They provide all features mentioned above and much more. If you develop an application to run in any of these application servers it will a) support multiple users by default; b) be able to connect to several database from different vendors (Oracle, MySQL, MSSQL); c) access web services (stack or rest); d) send emails; e) provide fameworks for logging, data access, user interface rendering; and f) manage multiple instances of the application server to optimize the use of available hardware, among other advantages. The figure below shows the graphical schema of an application server.

![cluster-300x262.png](/images/posts/cluster-300x262.png)

There are other kinds of middleware and I would like to emphasize a) <a href="http://en.wikipedia.org/wiki/Message_queue">message queue systems</a> (MQS) to mainly interchange asynchronous messages between applications; b) <a href="http://en.wikipedia.org/wiki/Enterprise_service_bus">enterprise service bus</a> (ESB) to integrate different kind of services provided by several systems; and c) <a href="http://en.wikipedia.org/wiki/Transaction_Processing_System">transaction systems</a> to guarantee the consistency of the data involved in the same business operation, such as database management systems.

Comparing middleware with framework and platform, I would say that a middleware system contributes to reduce the complexity of your application, which is one of the main characteristics of a framework, but it is not actually part of your application as a framework is. A middleware will provide many services for your application, but everything (middleware + application) will run on the available platform, which could be a virtual machine, or an operating system or a mobile device, etc.

I appreciate your questions and I love to answer them here! So, do not hesitate to post your comments as Hemanth did. Thanks for the opportunity to discuss the topic.
