---
layout: post
title: "Preparing Glassfish V2 for JSF 2.0"
date: 2009-10-06 20:27:00 +0200
categories: enterprise application software architecture web
---

I’m planning to migrate the web client of a JEE application from Apache Struts to JSF in order to reduce the complexity of the implementation and the number of required libraries. These libraries make the distribution package (ear) a giant file of 10MB, too much for a web application. 😛 However, since I don’t like JSF version 1.2 because of several design issues, I decided to wait a bit more for a stable release of JSF 2.0. I think I’m waiting too much :(. The first time I saw a presentation about JSF 2.0 was in December 2008, during the last edition of JavaPolis (now Devoxx), and since that time I haven’t seen any application server in its production release already available for this last JSF version.

Then I decided to make a little search on Google and I could find that JSF 2.0 RC can be configured to run on Glassfish V2/.1 without any complex step. Following the instructions of <a href="https://javaserverfaces.dev.java.net/nonav/rlnotes/2.0.0/releasenotes.html">this page</a>, I performed the following steps:

1. download the Mojarra 2.0.0 RC binary bundle from this <a href="https://javaserverfaces.dev.java.net/servlets/ProjectDocumentList?folderID=11662">webpage</a>;
2. backup your existing jsf-impl.jar found in GF_HOME/lib;
3. copy the new jsf-api.jar and jsf-impl.jar to GF_HOME/lib;
4. edit your GF_HOME/domains/[domain-name]/config/domain.xml and add (or update the existing classpath-prefix) ‘classpath-prefix=”${com.sun.aas.installRoot}/lib/jsf-api.jar” to the <java-config> tag;</java-config>
5. <domain-name>restart your server.</domain-name>

On your domain configuration file, domain.xml, set the classpath-prefix parameter as the example below:

{% highlight xml %}
<java-config
    classpath-prefix="${com.sun.aas.installRoot}/lib/jsf-api.jar"
    classpath-suffix="" ... >
  ...
  ...
</java-config>
{% endhighlight %}

Probably, you won’t find the classpath-prefix parameter there, so there is no problem if you add it. 😉 To check whether it is running correctly, open the Glassfish Admin Console (http://localhost:4848/), which is a JSF application, and see if it is running normally. The following line will be printed on the application server log file (server.log) when starting the JSF application:

    Initializing Mojarra 2.0.0 (RC b16) for context ''

That’s all! I’m not sure if it is enough. I’m going to start the migration in the next days. If I find issues during the process, I will come here to report them in details. I just hope that, when I finish this implementation, the market will finally offer an application server supporting JSF 2.0 by default.
