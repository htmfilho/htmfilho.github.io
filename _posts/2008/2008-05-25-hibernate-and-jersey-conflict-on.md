---
layout: post
title: "Hibernate and Jersey Conflict on Glassfish"
date: 2008-05-25 10:51:00 +0200
categories: enterprise application ide integration java jvm netbeans software architecture
---

Last weekend I tried to use [Jersey](http://jersey.dev.java.net) in an enterprise application to make some [RESTful](http://en.wikipedia.org/wiki/Representational_State_Transfer) web services available. The idea was to generate data to be plot by [flash charts](http://teethgrinder.co.uk/open-flash-chart/index.php). So, I created a new web module in addition to the already existent one. I thought it was better to keep it in a separate module to avoid changing the original web application,  since it still uses [Struts](http://struts.apache.org) as web framework. Before adding any RESTful web service, I just created the web application and deployed it successfully as an additional enterprise module. I’m happy about that because I will use the same strategy to migrate the web module from Struts to JSF, keeping the Struts version working in parallel to the JSF version, both sharing the same business logic.

I use [Netbeans](http://www.netbeans.com) because it makes my life easier. The Jersey module is available in the 6.1 version and for download in the update center for previous versions. Since installed, you may click with the right button on a web project to see the context menu and select “New … / RESTful Web Services from Patterns” or “New … / RESTful Web Services from Entity classes”. Since I’m not implementing entity classes in this module, I selected the one from patterns. It will start a wizard to prepare the application for REST and generate the initial class skeleton to start working.

I followed those steps and the RESTful web service was created successfully. However, when I start to deploy the whole application again, an obscure error appears in the Glassfish output log insistently. In such situation I tried everything: clean, build, clean and build, remove the module and deploy it separately, but nothing was enough to solve the problem below:

```
LifecycleException: java.lang.NoSuchMethodError:
  org.objectweb.asm.ClassReader.accept(Lorg/objectweb/asm/ClassVisitor;I)
(…)
Caused by: java.lang.IllegalStateException:
ContainerBase.addChild:
start: LifecycleException:
java.lang.NoSuchMethodError:
  org.objectweb.asm.ClassReader.accept(Lorg/objectweb/asm/ClassVisitor;I)
```

I checked if I was using the libraries appropriately, if they were correctly wrapped and if there was any library conflict. Yes, there is a library conflict with [Hibernate](http://www.hibernate.org/), the persistence framework I am using as a [JPA](http://java.sun.com/javaee/overview/faq/persistence.jsp) implementation. Jersey uses the [ASM library](http://asm.objectweb.org/), which is also used by Hibernate, but on different versions. Hibernate uses version 1.5.3 and Jersey uses 3.5.1. A big difference! We can not just delete the old version and put the new one there because they are architecturally different. Version 1.5.3 has an “attrs” package while 3.5.1 doesn’t have it but a “signatures” package. Changing the version can cause other problems and I’m not expecting them afterwards. So, how do I solve it consistently?

The ASM package is needed by the [cglib package](http://cglib.sourceforge.net/), which is part of the Hibernate libraries. If we remove that package, Jersey will work correctly, but Hibernate will stop working. To solve this conflict use cglib-nodep.jar instead of cglib.jar and keep ASM version 3.x with Jersey. cglib-nodep.jar includes some ASM classes demanded by cglib.jar, changing the package name to avoid any class conflict.

The ASM library is a Java bytecode manipulation and analysis framework. According to its website “(…) it can be used to modify existing classes or dynamically generate classes, directly in binary form. Provides common transformation and analysis algorithms to easily assemble custom complex transformations and code analysis tools“. ASM is used by many products like AspectJ, Oracle TopLink, JRuby, and many others. It can not be simply ignored by frameworks because it is a matter of flexibility. The best alternative is always to investigate the unexpected problem and claim for a better error presentation on the JVM.
