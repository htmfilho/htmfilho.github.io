---
layout: post
title: "Configuring Glassfish to Support Hibernate"
date: 2008-11-20 13:37:00 +0200
categories: uncategorized database enterprise application java
---

This is just a short post to remember how I prepared <a href="https://glassfish.dev.java.net/">Glassfish </a>to use <a href="http://hibernate.org/">Hibernate 3</a> as a JPA persistence framework.

The first step is to add Hibernate libraries in #glassfish_home#/lib . Those libraries are:

<ul>
<li>antlr-2.7.6.jar</li>
<li>c3p0-0.9.1.jar</li>
<li>cglib-nodep-2.1.3.jar</li>
<li>commons-collections-2.1.1.jar</li>
<li>commons-logging-1.0.4.jar</li>
<li>concurrent-1.3.2.jar</li>
<li>dom4j-1.6.1.jar</li>
<li>ehcache-1.2.3.jar</li>
<li>hibernate3.jar</li>
<li>hibernate-annotations.jar</li>
<li>hibernate-commons-annotations.jar</li>
<li>hibernate-entitymanager.jar</li>
<li>hibernate-validator.jar</li>
<li>javassist.jar</li>
<li>log4j-1.2.11.jar</li>
<li>ojdbc14.jar</li>
</ul>
All these libraries are distributed with Hibernate on this web page: <a href="http://hibernate.org/6.html">http://hibernate.org/6.html</a>. There are even more libraries available, but the set above was compiled by an attempt/error approach, which was indeed a tough task. You have to restart Glassfish in order to use those new libraries.

The next step is to create a connection pool and a JDBC resource, but I will assume that you know how to do that or you have read a post like <a href="http://blogs.sun.com/JagadishPrasath/entry/creating_jdbc_connection_pool_resource">the one written by Jagadish</a>.

Finally, you have to configure your persistence unit in order to use Hibernate. See parts of my persistence.xml file below:<br/><span style="font-size:85%;"><br/><span style="font-family:courier new;">‹persistence version=”1.0″ </span><br/><span style="font-family:courier new;">    xmlns=”http://java.sun.com/xml/ns/persistence” </span><br/><span style="font-family:courier new;">    xmlns:xsi=”http://www.w3.org/2001/XMLSchema-instance” </span><br/><span style="font-family:courier new;">    xsi:schemaLocation=”http://java.sun.com/xml/ns/persistence </span><br/><span style="font-family:courier new;">        http://java.sun.com/xml/ns/persistence/persistence_1_0.xsd”›</span><br/><span style="font-family:courier new;">    ‹persistence-unit name=”#persistence-unit-name#” transaction-type=”JTA”›</span><br/><span style="font-family:courier new;">        ‹provider›org.hibernate.ejb.HibernatePersistence‹/provider›</span><br/><span style="font-family:courier new;">        ‹jta-data-source›#jdbc-datasource#‹/jta-data-source›</span><br/><span style="font-family:courier new;">        ‹class>#persistence-class#‹/class›</span><br/><span style="font-family:courier new;">        … ‹!– Your persistence classes –›</span><br/><span style="font-family:courier new;">        ‹exclude-unlisted-classes›true‹/exclude-unlisted-classes></span><br/><span style="font-family:courier new;">        ‹properties›</span><br/><span style="font-family:courier new;">            ‹property name=”hibernate.dialect” </span><br/><span style="font-family:courier new;">                value=”org.hibernate.dialect.Oracle10gDialect”/›</span><br/><span style="font-family:courier new;">            ‹property name=”hibernate.show_sql” value=”false”/›</span><br/><span style="font-family:courier new;">            ‹property name=”hibernate.cache.provider_class”</span><br/><span style="font-family:courier new;">                value=”org.hibernate.cache.HashtableCacheProvider”/›</span><br/><span style="font-family:courier new;">        ‹/properties›</span><br/><span style="font-family:courier new;">    ‹/persistence-unit›</span><br/><span style="font-family:courier new;">‹/persistence›</span></span>

Basically, you have to set the provider tag with “org.hibernate.ejb.HibernatePersistence” and set some properties according to specific needs. That’s all!
