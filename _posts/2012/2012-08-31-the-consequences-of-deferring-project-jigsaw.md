---
layout: post
title: "The Consequences of Deferring Project Jigsaw"
date: 2012-08-31 09:33:00 +0200
categories: java javafx jvm operating system software architecture strategy
---

Mr. Mark Reinhold has <a href="http://mreinhold.org/blog/late-for-the-train" target="_blank">announced in July 2012</a> that they were planning to withdraw <a href="http://openjdk.java.net/projects/jigsaw/" target="_blank">Project Jigsaw</a> from Java 8 because Jigsaw would delay its release, planned for September 2013 (One year from now). This date is known because Oracle has decided to implement a two years roadmap planning for Java, so September 2013 is actually 2 years after the release of Java 7.

According to Jigsaw’s website…

> “The goal of this Project is to design and implement a standard module system for the Java SE Platform, and to apply that system to the Platform itself and to the JDK. The original goal of this Project was to design and implement a module system focused narrowly upon the goal of modularizing the JDK, and to apply that system to the JDK itself. The growing demand for a truly standard module system for the Java Platform motivated expanding the scope of the Project to produce a module system that can ultimately become a JCP-approved part of the Java SE Platform and also serve the needs of the ME and EE Platforms.”

They also say:

> “Jigsaw was originally intended for Java 7 but was deferred to Java 8.”

Now they want to defer it to Java 9 🙁 More details of their decision making are available in a [Q&amp;A post on Reinhold’s blog](http://mreinhold.org/blog/late-for-the-train-qa). You may read and follow the discussion there. Here is my opinion:

Without Jigsaw, I believe that it’s very difficult to put Java everywhere. Without Jigsaw, the idea of multi-platform is getting restricted to servers in a age of smartphones and tablets. Jigsaw may be “late for the train”, but it is letting Java late for the entire platform ecosystem.

![java-everywhere-300x227.png](/images/posts/java-everywhere-300x227.png)

Observing the market, we can see that development is becoming platform-dependent (iOS, Android, etc.) Only Java can beat this trending because of its large experience on multiplatform implementation, and the time to do it is NOW! Otherwise, in 3 or 4 years there will be no Java on devices, and the development community will have enough knowledge to live with that. Therefore, Java will be basically a server-side technology.
