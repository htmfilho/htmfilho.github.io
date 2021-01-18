---
layout: post
title: "Accessing an Embedded Database Using JPA in a Desktop Application"
date: 2008-11-16 13:56:00 +0200
categories: database java jvm research
---

The problem of developing an unusual application is that we spend most of the time thinking about the architecture. Every single additional code is a big decision, unless you are not so obsessed like me. When you are developing a traditional web application or an enterprise application the architecture definition is relatively easy because there are many references available to inspire you, like specialized books, professional blogs, speakers, frameworks ready to use, and so on. On the other hand, when you are developing something new, like an innovative framework, a device driver or a concurrent application (which is my case), architecture is your main concern, isn’t it?

My open source project (<a href="http://kenai.com/projects/meanings4fusion">Meanings4Fusion</a>) is consuming all my thoughts on its architectural definition. At the same time, I’m working hard on its implementation  because I have a deadline in early December and also because an active open source project may attract more people in a short term, as soon as our solutions become solutions for their problems too. For instance, you probably might be interested to know how to embed a database in your application in order to distribute it without any further installation and store data without the complexity of manipulating files or network connections. My experience was very frustrating because of the lack of information available about this problem, but now, taking some assumptions and attempts, it was much easier than I was expecting.

In order to have this facility I have made some choices:

- <span style="font-weight: bold;">considering JVM version 6 or superior</span>: sorry for those who use Mac, but I prefer a free software world than a world of limited freedom. But, don’t worry, Java 6 will be available for you soon, of course, as soon as Mac guys decide to finish it, because <a href="http://www.sun.com/">SUN</a> can’t do anything to help you in a proprietary system. Java 6 is faster and implements many cool things that we might need in the project.

- <span style="font-weight: bold;">using Java DB</span>: it is actually <a href="http://db.apache.org/derby/">Apache Derby</a> with a new name. If you use Derby instead the final result will be the same. Even the configuration stuff is valid for both. Java DB can be used as a server or embedded, which is our case. Embedded, it executes in the same process of the application and may add some delay when you access the database for the first time, but it is just at the beginning, normalizing later.

- <span style="font-weight: bold;">using JPA (Java Persistence API)</span>: using a database nowadays is not a complex task anymore, neither to embedded databases. As I mentioned <a href="http://planexstrategy.blogspot.com/2008/11/annoying-unchecked-conversion-using-jpa.html">before</a>, JPA simplifies the code to access the database keeping its elegance and focus on the main problem. I picked Toplink essentials because of its small size, but I don’t like it. With more time I will change to <a href="http://www.eclipse.org/eclipselink/">Eclipse Link</a>.

I’m writing a lot, but we don’t have much to do. Just enjoying the opportunity to talk more with you. Basically, you have to add 3 more libraries within your project. To embed the database, add derby.jar (available at <a href="http://db.apache.org/derby/">http://db.apache.org/derby/</a>). To use JPA, add toplink-essentials.jar and toplink-essentials-agent.jar (available at <a href="http://oss.oracle.com/toplink-essentials-jpa.html">http://oss.oracle.com/toplink-essentials-jpa.html</a>). This is 40% of all you have to do.

![embedded.png](/images/posts/embedded.png)

The next step is to create the file persistence.xml in the directory META-INF, which should be packaged within your application (jar file). The content of the file is available <a href="http://kenai.com/projects/meanings4fusion/sources/1193/content/src/META-INF/persistence.xml?id=1193-Subversion-Source-Code-Repository">here</a>. At this line – <span style="font-style: italic;">property name=”toplink.jdbc.url” value=”jdbc:derby:meanings4fusion;create=true”</span> – be aware of “create=true”. It will automatically create a database if it doesn’t exist yet. Something else important is this line – <span style="font-style: italic;">property name=”toplink.ddl-generation” value=”create-tables”</span> – which specifies the automatic creation of tables according to the implemented entity classes. This step represents 20% of everything. We are almost there.

Now, you have to implement an entity class and some methods for it to persist it when necessary. An example is available <a href="http://kenai.com/projects/meanings4fusion/sources/1193/content/src/org/meanings4fusion/core/Ontology.java?id=1193-Subversion-Source-Code-Repository">here</a>. The correspondent table for the Ontology entity (example) will be automatically generated in its first use. It is important to add as much information about the metadata as possible in the annotations of the entity class because it will generate a better database structure. A standalone application cannot use the transaction manager from a container, which obliges us to start, commit and, if needed, rollback a transaction.

So, Done. 100%.
