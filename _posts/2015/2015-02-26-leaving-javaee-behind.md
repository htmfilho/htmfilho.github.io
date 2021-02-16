---
layout: post
title: "Leaving JavaEE Behind"
date: 2015-02-26 23:56:33 +0200
categories: community java java ee
---

I’ve been a Java EE supporter for years. In practice, I’ve been using it since the beginning and evangelizing it since 2011 through an open source project called Yougi. This app is currently used to manage the CEJUG community, thus equally useful to manage any kind of communities on-line. But, above all, this project was intended to teach Java EE, giving real world examples of code that people could simply copy and paste in their projects, thanks to its liberal open source license. I believe this project has served its purpose, since it has been forked more than 60 times on GitHub, stared more than 20 times and received contributions from 16 developers. But today, I’m going to tell you a different story. A story that explains why I’m not going any further with Java EE.

<a href="http://www.hildeberto.com/wp-content/uploads/2015/02/complexity.png">![complexity-1024x668.png](/images/posts/complexity-1024x668.png)</a>

<h3>Why Am I Not Going Any Further With Java EE?</h3>

By September 2013, I was fairly happy with Java EE platform. I was convinced Java EE was in the right track since its complexity was going away (not really… they just hid it with lots of annotations) and many Spring developers were migrating to it. At that time, I had all the arguments to jump into long discussions in favor of Java EE. However, two recent events have diminished my motivation to keep evangelizing it:

1. <em><strong><a href="http://www.hildeberto.com/2013/11/glassfish-is-now-a-javaee-toy.html" target="blank" title="Glassfish Is Now A JavaEE Toy">Oracle downgraded Glassfish from a product to a basic JavaEE reference implementation</a></strong></em>: Glassfish was an excellent product but Oracle’s sales team never gave the necessary attention to it and the project became unsustainable. So, by the end of 2013, Oracle decided to stop supporting it. Does it make any difference? Yes, it does. Glassfish gets out of the competitive market, so they don’t solve bugs fast enough and performance isn’t a serious concern anymore. I was using Glassfish at work and at home, for personal projects. So, that means I had to migrate everything to another application server sooner or later.

2. <em><strong>Migrating from Glassfish to another certified JavaEE server was a nightmare</strong></em>: at first we thought the migration would be easy because we maximize the use of the Java EE specification and minimize dependencies on third-part libraries. However, the migration was so hard that we aren’t even close to finishing it. Libraries and frameworks that follow JavaEE specifications actually behave differently in some aspects that are not sufficiently covered by TCKs (<a href="https://jcp.org/en/resources/guide-tck" target="blank">Technology Compatibility Kit</a>). When the team writes software exploring exactly those uncovered behaviors, then the migration becomes a nightmare.

Furthermore, the constant addition of new JSRs (Java Specification Request) to the Java EE specification is actually harming the ecosystem because:

- It’s slowing down companies and open source communities to catchup with new developments and tests to become Java EE certified. For instance, the Java EE 7 specification was released in June, 2013. Many app servers are already certified, but we are in February, 2015 and there is no official support provided to those certified servers. So, the TCKs do not guarantee production-ready implementations, which indicates that those tests are superficial.

- open source communities have to create projects totally from scratch, just to become Java EE compliant. It’s a terrible use of voluntary work. People are wasting their time on constantly reinventing the wheel.

- some implementations are reused in several app servers and they are rewritten only when their open source licenses are incompatible with other dependencies. It proves that some JSRs have weak motivations to exist, since there is no real competition in some cases.

- when Java EE implementations are put together, they create a huge complex stack, generating several failure points while trying to make them work together. The more JSRs, the higher the likelihood of bugs and strange behaviors.

<h3>Parasitic Problems</h3>

With all that complexity comes also the traditional issues that continue indefinitely unsolved:

<strong>Constant redeployments</strong>: while the redeployment issue is definitely solved in Ruby on Rails, Python, PHP, Play, Clojure, ASP.Net and others, it is still an issue in the JavaEE platform. This problem is there for so long that a business focused on handling that was created. <a href="http://zeroturnaround.com" target="blank">ZeroTurnaround</a> invented JRebel and LiveRevel to minimize redeployments, thus increasing developers productivity. JRebel is a must-have because we constantly lose concentration while the app is redeploying. The waste of time is so heavy without it that JRebel pays itself in a couple of days.

<strong>Scalability limitations</strong>: for this point I just quote <a href="https://twitter.com/karianna" target="blank">Martijn Verburg</a> in one of his <a href="https://www.parleys.com/talk/the-lean-start-up-ninja" target="blank">Devoxx talks</a>:

> “Traditional JavaEE servers and the technology stack they support don’t scale for the cloud, they don’t scale for the web, not quite yet. Java EE 7 and things like WildFly, supporting micro-kernel and micro-containers is getting a lot better, but if we want to horizontally scale, there is no way we are going to deploy a hundred WebLogics, a hundred Webspheres across our nodes. It’s never going to work, right? There is too much lusts and fluffs involved in those big stacks”.

<strong>Java</strong>: that’s probably the most verbose language right behind C++. Considering the current offering of programming languages on the JVM, Java is certainly the least productive. It’s actually impossible to earn any money at all without a IDE. All relevant frameworks require you to write getters and setters for classes attributes, otherwise they won’t be able to break classes encapsulation with reflection. Even for simple things you have to write classes and when the amount of classes is not enough, some design patterns will require you write even more classes. At the end of the day, you have more classes than the abstractions of the “real world” you wanted to represent with object orientation. All specifications managed by the JCP most be written in Java, and since JavaEE is a huge state machine, other languages running on the JVM have issues sharing those states.

<strong>Source of inspiration outdated</strong>: JavaEE evangelists claim that JavaEE is attracting many Spring developers because it finally reached Spring’s innovations with simplicity. However, Spring is already an outdated technology in comparison to reactive frameworks like AKKA and web frameworks like Play. If JavaEE keeps its bad referential, it will soon stagnate, as pointed out by <a href="http://www.ing.jobs/Netherlands/Expertise/Information-Technology/Blog/Ron-van-Kemenade-8.htm" target="blank">Ron van Kemenade</a>, CEO ING Group, during his <a href="https://www.parleys.com/talk/the-end-traditional-enterprise-it" target="blank">Devoxx’s talk</a>:

> “The traditional IT vendors, they don’t offer you that. They stick to their old paradigms of whatever they sell you: the enterprise class, they say. Only in my case it always fails.”

<strong>It isn’t purely technical, it also comes with legal concerns</strong>: JavaEE specs are very conservative, don’t target innovation and have huge legal concerns from companies that contribute to the JSRs. Intellectual property is an issue constantly mentioned in JCP presentations. What they didn’t realize yet is that nobody cares about Java intellectual property since it doesn’t have innovation as a goal and after Microsoft released a multi-platform .Net Framework under Apache license.

<h3>Is there a way to save JavaEE from self-destruction?</h3>

Unfortunately not. Besides everything I listed above, better alternatives will be so common and mature that applications using JavaEE will enter in maintenance mode in about three or four years time. JavaEE 7 was released on 2013 and there is no official support for it until now, 1 1/2 years later. If JavaEE 8 is released in 2016, then it will be probably available in 2018 only. So, in 2018 developers will be able to do just a little bit of cloud development, while other stacks are mastering the art of scalability. There is no sign so far that JavaEE 8 will take advantage of the new Java functional capabilities. It will be probably postponed to JavaEE 9, finally available in 2021. Of course, they didn’t have time to consider the new Java 9 features, thus real modularity will be available only in 2024, almost ten years from now. This timeline does make sense because if you look back 10 years ago, J2EE was actually impractical and Spring was conquering the world, but this time the competition will be relentless.

By the way, current players will be just fine, because they are already creating strong alternatives to JavaEE (Example: VertX by RedHat and several other Apache projects).
