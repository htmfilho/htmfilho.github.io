---
layout: post
title: "Platform versus Framework"
date: 2008-10-12 20:03:00 +0200
categories: integration java jvm open source operating system research software architecture user interface
---

In the last 30 days I had the pleasure to work in the context of the <a href="http://www.openinterface.org/">OpenInterface</a> project, writing a document that delineates how the platform will continue after the project period. They thought I could help because of my long experience with the open source community. Actually, it was a great challenging experience with hard and pleasant moments. The most exciting one was in Porto, Portugal, on the border of the river, when I found inspiration to write some killer sentences.

During the elaboration of this document, many people from the project gave contributions, comments, critics, which was essential to get a better result at the end. But one of them called my attention. One of the contributors, asked to change the term <span style="font-style: italic;">platform</span> to <span style="font-style: italic;">framework</span>, which was funny because the name <span style="font-style: italic;">platform</span> is spread through many other documents and on the website. So, the person had some fundamentals to propose this change. What are they? Then I decided to make a short research about the difference between both concepts and the best place to start is, of course, the dictionary.

The word <span style="font-style: italic;">platform</span> has many meanings, including the computer science one. In the Cambridge English Dictionary:

> “Platform describes the type of computer system you are using, in connection with the type of software you can use on it.”


This is a very generic definition, which doesn’t help me at all. So, I went to Wikipedia, where I found a definition without any alert about its sources or impartiality:

> “In computing, a platform describes some sort of hardware architecture or software framework (including application frameworks), that allows software to run. Typical platforms include a computer’s architecture, operating system, programming languages and related runtime libraries or graphical user interface.”


Oh God! It mentions framework on the definition of platform. Is it some sort of recursive definition? Well, let’s go to the framework’s definition:

> “A software framework is a re-usable design for a software system (or subsystem). A software framework may include support programs, code libraries, a scripting language, or other software to help develop and glue together the different components of a software project. Various parts of the framework may be exposed through an API.”


<iframe align="left" frameborder="0" marginheight="0" marginwidth="0" scrolling="no" src="http://rcm.amazon.com/e/cm?t=c03ce-20&amp;o=1&amp;p=8&amp;l=bpl&amp;asins=0471248754&amp;fc1=000000&amp;IS2=1&amp;lt1=_blank&amp;m=amazon&amp;lc1=0000FF&amp;bc1=000000&amp;bg1=FFFFFF&amp;f=ifr" style="align: left; height: 245px; padding-right: 10px; padding-top: 5px; width: 131px;"></iframe>Well, better! Let’s analyze the differences. First: framework refers only to software and ignores hardware totally. So, if you work with hardware it will never have a framework ;-). Second: a platform allows a software to run, which is not a framework requirement, since it is more focused on design. For instance, <a href="http://java.sun.com/">Java</a> is a platform because it has a virtual machine that allows Java applications to run in many operating systems. On the other hand, <a href="http://www.springframework.org/">Spring</a> is a framework because it simplifies the way you design software, taking the responsibility for a lot of things to reduce the effort and the volume of code needed to implement the application. So, a platform doesn’t aim to save your time, but to give you one or more possibilities to run your application.

Going back to the root of the discussion, I had a long conversation with the main developer of the OpenInterface (OI), Lionel Lawson, and we concluded that OI is, at the same time, a platform and a framework. It means that, when platform, OI can run your application on it. When framework, your application can use the OI’s API to access other components. Then, we concluded that OI is actually a technology, which is more generic and solves many integration problems between low level components.
