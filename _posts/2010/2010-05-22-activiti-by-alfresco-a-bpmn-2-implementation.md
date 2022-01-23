---
layout: post
title: "Activiti by Alfresco: A BPMN 2 Implementation"
date: 2010-05-22 12:37:00 +0200
categories: business process java
---

I’m giving a try on the recent open source project [Activiti](http://www.activiti.org/), which implements BPMN 2 (Business Process Management Notation). Despite being in its first alpha version, Activiti already called [a lot of attention](http://www.jorambarrez.be/blog/2010/05/19/reactions-to-the-activiti-launch/) from the community. I think it is due to the fact that the leaders are quite reliable people. They are former [JBoss](http://www.jboss.org/)' employees, who created and maintained the [JBPM](http://www.jboss.org/jbpm) project, a business process management framework, and it is quite successful nowadays.

I’ve met [Tom Baeyens](http://processdevelopments.blogspot.com/) and [Joram Barrez](http://www.jorambarrez.be/blog/) in the last edition of [Devoxx](http://devoxx.com/). Their talks were a “must attend” section in all recent Devoxx editions, and they will probably present their brand new product  at this year’s edition too. The framework is still in alpha but I think it will evolve a lot until there. By the way, the current version is more about playing and understanding the idea than effectively performing processes. What I’ve seen so far deserves some comments.

My first impression was nice. Activiti is very simple to install and the team made a very good work on the design of the user interfaces. Of course, I cannot be so critical right now because it is just beginning, but I will follow the project from now on to give constructive feedbacks to the team.

![Screenshot-Activiti-Explorer-Tasks-Google-Chrome-300x192.png](/images/posts/Screenshot-Activiti-Explorer-Tasks-Google-Chrome-300x192.png)

On the other hand, I was expecting something different, simpler, like a process engine 100% controlled by REST web services. I don’t like the fact of a web application handling the processes execution (screenshot above). Using Activiti Explorer, you can start processes and perform their activities, but it forces the user to be aware of processes’ details. I think an application that implements a business process should be more focused on:

- the performance of the user when executing his/her activities; and

- the quality of the data inserted.

Better to wait a little bit more to see the Activiti evolution. I do support the project and hope to see it widely adopted.
