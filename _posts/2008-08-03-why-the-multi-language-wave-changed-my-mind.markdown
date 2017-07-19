---
layout: post
title: "Why the Multi-language Wave Changed my Mind"
date: 2008-08-03 08:28:00 +0200
categories: integration java php software architecture web
---

You can notice that I’m deeply involved with Java if you read my posts. Java is so powerful and complete that I haven’t needed anything else in the last 8 years. I could develop everything, from academic works to widely distributed systems, thus I can consider me as a master in Java.

Suddenly, with a strong influence from the <a href="http://agilemanifesto.org/principles.html">Agile Manifest</a> and from the <a href="http://domaindrivendesign.org/">Domain-Driven Design</a>, people started to program using many other languages outside the Java/.NET world. Groove, Ruby, PHP, Python, JavaScript, Scala, and many others won their own space and their adoption is growing every day.

Until some months ago, I was not yet convinced about the need for a language different from Java, since all my programmer abstractions are perfectly mapped to the Java technology. I realized my blindness when I saw how much I paid to use the infra-structure of my application service provider. Every single month I’ve paid something around US$30/month. It is too expensive for a very simple website. Then I realized that if I do the same thing using PHP or Ruby, instead of JSP running in a complex environment like Tomcat, I can reduce my costs to US$6/month! :O That’s a good reason to scape from Java sometimes. Actually, I thought the same in the past, but I didn’t do it because of a feeling of guilty, the guilty of developing a non-object oriented application, limited in terms of connectivity, extensibility, robustness, etc. The wave of learning multiple languages taught me that adopting a new language for a certain kind of problem could be more cost effective than forcing the use of Java technology.

Now, I’m learning PHP to develop the website of <a href="http://www.mentores.com.br/">my company</a> (small but still a company). I hope you don’t mind. I have to say it’s pretty annoying for me to migrate from a well designed language to a quite <a href="http://www.codinghorror.com/blog/archives/001119.html">scaring and messy language like PHP</a>, but it doesn’t matter when the cost is a concern.

Because I’m still conservative, I do not recommend PHP for developing products, internal applications or when there is high availability of infra-structure. Believe me: you will need some level of integration with your existent applications and with applications of your partners and costumers. Adopting a new language is a matter of responsibility and common sense.
