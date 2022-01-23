---
layout: post
title: "Jersey and JSF Conflict caused by Netbeans"
date: 2010-03-23 16:14:00 +0200
categories: enterprise application ide integration java netbeans software architecture web services
---

Have you noticed that JSF 2.0 has a new pre-defined directory called “resources” that is located in the web content? According to [JavaServer Faces 2.0, The Complete Reference](http://www.amazon.com/JavaServer-Faces-2-0-Complete-Reference/dp/0071625097?ie=UTF8&amp;tag=c03ce-20&amp;link_code=btl&amp;camp=213689&amp;creative=392969), “_files in this directory are treated specially by the JSF Runtime. (…) files and directories within the /resources directory are intended to be included in other pages in the application. Content here can be images, stylesheets, and composite components._“. Therefore, if your Java web application has a /resources directory with a different meaning, then you have to consider renaming it to avoid conflicts when migrating to JSF 2.0.

But there are more conflicts to deal with. I was having some relaxing time programing my JSF 2.0 application ([Yasmim](http://github.com/htmfilho/Yasmim)) on Saturday night when I decided to implement some RESTful web services. Knowing that Netbeans is like a Swiss army knife when developing JEE applications, I went into its special features to support the JAX-RS specification ([JSR 311](http://jcp.org/en/jsr/summary?id=311)) and I could get most of the necessary configuration done automatically. However, this automation causes a conflict with the JSF application if you don’t pay attention to a simple detail shown in the figure below.

![Screenshot-REST-Resources](/images/posts/Screenshot-REST-Resources-Configuration-300x157.png)

The field “REST Resources Path” has the default value “/resources”. This path is used in the application URL to denote the invocation of RESTful web services. For instance, in the URL “http://localhost:8080/yasmim/resources” anything after “/resources” is considered as a RESTful web service. If something after “/resources” is not correctly mapped, then a HTTP error occurs. This is actually a good practice because the key abstraction of information and data in REST is a resource. Representing it in the URL makes it clear.

However, when the application also uses the JSF 2.0 framework, this REST resource path conflicts with the JSF resources directory. As a consequence, files in the resources directory obviously are not mapped as services and won’t be available for JSF pages. In practice, CSS and script files become unavailable, destroying the design and layout of the website.

To solve this conflict, we have to change the proposed resource path to another value. In my case, I’m  using “/service”, which is still coherent because REST is a style of web service implementation. After changing this value you have to clean and rebuild the project and redeploy the application because hot deployment in Glassfish doesn’t work in this case.
