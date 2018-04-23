---
layout: post
title:  "Against Easy Architecture Thinking"
date: 2018-04-13 12:00:00 +0200
categories: python architecture asynchronous osis
---

![Inexperienced Developer](/images/posts/easy-architecture-thinking.png)

Easy vs. simple.

Sharing a database as a system integration versus queuing.

The number of possible users does not necessarily correspond to the demand of a system. Other systems are also part of the demand, and systems are usually greedy.

Do you like to be blamed for something that is not your fault? That's what happens when the database is down because of a third part application.

Queuing is not complicated. It is extremely simple, but people can make it complicated.

Queuing within programming context, not even outside.

<!-- more -->

Describe why message queuing is important for osis and why a database replication should not be used to replace it, as some may think.

Asynchronous data exchange.
Data Model independent.
High availability.
Decoupled.
