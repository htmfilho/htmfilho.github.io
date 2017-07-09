---
layout: post
title: "Development Environment to Work with WebLogic"
date: 2011-09-24 16:15:00 +0200
categories: uncategorized enterprise application ide java ee workspace
---

I have to confess that, despite not evolving as fast as the Java EE specification, Oracle WebLogic is a f*** good application server. Its stability is impressive and works smoothly with popular IDEs, such as Eclipse and Netbeans. Of course its qualities come with a cost, which is expensive for poor developers like us, but it’s worthwhile for companies.

The official name of WebLogic is “Oracle WebLogic Server 11g Standard Edition”. It is part of a broader range of products called “Oracle Fusion Middleware”, which offers a complete support for enterprise service-oriented applications (SOA). I’m currently working with WebLogic 10.3.4, which is the first version that supports JSF 2.0, my favority web framework. WebLogic is available for download on Oracle’s website. Go to the <a href="http://www.oracle.com/technetwork/middleware/fusion-middleware/downloads/index.html">download page</a> to get your copy. To install it:

<ol>
<li>Unzip the file in your development folder. For example <i>/home/you/java/weblogic</i>. </li>
<li>Create the environment variable <i>JAVA_HOME</i>, pointing to your JDK installation.</li>
<li>Create the environment variable <i>MW_HOME</i> pointing to <i>/home/you/java/weblogic</i>. </li>
<li>Go to the command line and run the installation configuration script <i>$MW_HOME/configure.[sh/cmd]</i>. </li>
<li>Create the domain to start working with WebLogic, running the command <i>MW_HOME/wlserver/common/bin/config.[sh/cmd]</i> and following the instructions on the screen. </li>
<li>Start a web browser and open the url <i>http://localhost:7001/console</i> to access the administration console.</li>
</ol>
<h3 sizcache="2" sizset="70"> <a href="http://www.blogger.com/blogger.g?blogID=1281882577011517327&amp;pli=1" name="Architecture-Howto-JavaDevelopmentEnvironment-ChangingWeblogicClasspath"></a></h3>
<div sizcache="2" sizset="71">Now, we have to configure the IDE to start, debug, and stop WebLogic, as well as deploy Java EE applications. Because most developers actually use Eclipse as a working IDE, let’s configure it, installing the necessary plugin. I’m using <a href="http://www.oracle.com/technetwork/developer-tools/eclipse/downloads/index.html">Oracle Enterprise Pack for Eclipse (OEPE)</a>, a plugin that empowers Eclipse to develop Enterprise Java Application for Oracle Products. To install it:</div