---
layout: post
title:  "Loosely Coupled Apps With RabbitMQ"
date: 2018-04-13 12:00:00 +0200
categories: python rabbitmq asynchronous queue decoupling singlepointoffailure availability performance
---

![Inexperienced Developer](/images/posts/easy-architecture-thinking.png)

Highly coupled monolithic application with multiple responsibilities.
Coupled apps using web services.
The problem of database as a single point of failure.
Decoupling apps using queues to share data.

Tasks
  1. Disabling queues when exclusively working in one of the applications
  2. Enabling queues when working in both applications
  3. Disabling queues when running unit tests

What you are doing is throwing high availability, loosely coupling, performance, and the single responsibility principle in the trash because you are a lazy learner. You want to keep things easy, using the database as integration platform to favor of your own confort, instead of favoring the mission of the organization.
