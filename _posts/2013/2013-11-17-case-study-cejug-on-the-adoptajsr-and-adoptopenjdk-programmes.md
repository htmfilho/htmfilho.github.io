---
layout: post
title: "Case Study: CEJUG on the AdoptaJSR and AdoptOpenJDK Programmes"
date: 2013-11-17 23:37:19 +0200
categories: analytics community jcp jsr jug openjdk
---

CEJUG, one of the most active JUGs in Brazil, decided to join the programmes [AdoptaJSR](https://java.net/projects/adoptajsr/pages/Home) and [AdoptOpenJDK](https://java.net/projects/adoptopenjdk) in January 2013, led by [Helio Frota](http://heliofrota.github.io/) and myself. These programmes are jointly managed by the [London Java Community](http://www.meetup.com/Londonjavacommunity/), UK (LJC) and [SouJava](http://soujava.org.br), Brazil. **An initiative from the community for the community to transform passive java users into active java contributors**. The programmes target java specifications, namely JSRs (Java Standard Request), and the [OpenJDK](http://openjdk.java.net/), an open source implementation of the Java Development Kit.

Moved by a great excitement, CEJUG also joined the [Java Community Process](http://jcp.org/en/home/index) (JCP) by February 2013. They believed that if they manage to give concrete contributions then it would help them to push those into future releases. If it happens at least once, then it would be a great achievement for the local community.

In addition to the OpenJDK, CEJUG also decided to adopt the following JSRs:

- [Java API for RESTful Web Services 2.0 (JSR 339)](http://jcp.org/en/jsr/detail?id=339)
- [JavaServer Faces 2.2 (JSR 344)](http://jcp.org/en/jsr/detail?id=344)
- [Java API for Json Processing (JSR 353)](http://jcp.org/en/jsr/detail?id=353)
- [Java API for WebSocket (JSR 356)](http://jcp.org/en/jsr/detail?id=356)

JUG leaders, together with active members, have communicated the programme to the community in an event that happened in March, 2013. They picked up those JSRs and asked people to look around, test the API and give some feedback about what they were looking at. They clearly stated that every single feedback matters, even simple things like readability, clarity, completeness, and so on.

Unfortunately, apart from the community leaders, very little effort was spent by members on the programmes. Action was missing indeed. CEJUG was not putting into practice the expertise shared by other JUG leaders. In any case, leaders and active members heroically gave contributions almost exclusively to the AdoptOpenJDK programme:

1. [Event launching the programmes AdoptaJSR and AdoptOpenJSR](http://www.youtube.com/watch?v=X93VmOAN4Js&amp;feature=share&amp;t=45m52s)
2. [Event TecTel IFCE Tauá](http://www.cejug.org/2013/06/08/evento-tectel-ifce-taua/)
3. [Reduced the required memory to build the OpenJDK 8](https://java.net/projects/adoptopenjdk/pages/YourOwnEnvironment)
4. [Issue created: JavaDoc problems when building with OpenJDK 8](https://java.net/jira/browse/JSON_PROCESSING_SPEC-59)
5. [Logo that can be used by projects that run on Java 8](http://www.cejug.org/2013/07/16/logo-oficial-para-projetos-compativeis-com-java-8/)
6. [Discussion about the inclusion of the method isEmpty in the class StringBuilder](/2013/05/look-at-it-carefully-and-you-will-find.html)

Some months later, they realised, during informal talks to some active members, the word “Adopt” was too heavy for them. It might be a cultural thing, but they understood that as “Taking Care”. It sounded like they would need to allocate quite a lot of time to make something relevant to finally give a feedback. They felt somehow constrained by the responsibility of “taking care” of something so globally relevant.

Time passes. Glassfish 4 was released. All JSRs they have adopted went final. After that, they felt some activity gaps from the programme. Meanwhile, folks quietly started playing around with JSRs, not in the context of the programme, but because of their jobs, PoCs, training, university courses, etc. They were keeping that for themselves until a day in October 2013 when a member discussed an issue in the mailing list. That was the tipping point that moved others to report their own issues as well. The issues were in a much smaller granularity than an usual adoption case we’re used to see in the programmes. Smaller in terms of impact, but when put together they could actually be considered relevant.

This time, the contributions sounded more concrete, visible and with positive feedback from spec leaders and implementation leaders. That’s what they did in an one month period:

1. [Issue created: Request parameters lost after realm form authentication to access a protected page](https://java.net/jira/browse/GLASSFISH-20809)
2. [Reviewed and Improved the Text of the JSR 354 Spec](http://jcp.org/en/jsr/detail?id=354)
3. [Issue created: Sequence of adding a JsonArrayBuilder into a JsonObjectBuilder interferes in the final result](https://java.net/jira/browse/JSONP-24)
4. [Issue created: @NotNull check fails in String attribute when using group validation](https://hibernate.atlassian.net/browse/HV-831)
5. [No alternative for @ManagedProperty to get Request Parameters](https://java.net/projects/javaserverfaces/lists/users/archive/2013-10/message/12)
6. Partnership with Bulgarian JUG to resume collaboration on the AdoptOpenJDK programme (on going)

In summary, it was practical and realistic for the CEJUG community to give smaller contributions to several JSRs without the heavy “adopt” label. At the same time, they don’t want to pass the message that the word “Adopt” should be replaced. Actually, the names of the programmes sound good and they are well disseminated. However, CEJUG does suggest that “adopt” should be kept in an umbrella level, and “contribute” could be a term used to define actions taken by JUGs on JSRs. Therefore, instead of saying “We’re adopting the following JSRs” we could say “We’re contributing to the following JSRs”.

**CEJUG strongly believes that by transforming community members from passive consumers to active contributors, they are concretely moving Java Forward!**
