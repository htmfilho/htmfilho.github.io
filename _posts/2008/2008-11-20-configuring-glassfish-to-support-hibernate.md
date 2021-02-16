---
layout: post
title: "Configuring Glassfish to Support Hibernate"
date: 2008-11-20 13:37:00 +0200
categories: database enterprise application java
---

This is just a short post to remember how I prepared <a href="https://glassfish.dev.java.net/">Glassfish</a>to use <a href="http://hibernate.org/">Hibernate 3</a> as a JPA persistence framework.

The first step is to add Hibernate libraries in #glassfish_home#/lib . Those libraries are:

- antlr-2.7.6.jar
- c3p0-0.9.1.jar
- cglib-nodep-2.1.3.jar
- commons-collections-2.1.1.jar
- commons-logging-1.0.4.jar
- concurrent-1.3.2.jar
- dom4j-1.6.1.jar
- ehcache-1.2.3.jar
- hibernate3.jar
- hibernate-annotations.jar
- hibernate-commons-annotations.jar
- hibernate-entitymanager.jar
- hibernate-validator.jar
- javassist.jar
- log4j-1.2.11.jar
- ojdbc14.jar

All these libraries are distributed with Hibernate on this web page: <a href="http://hibernate.org/6.html">http://hibernate.org/6.html</a>. There are even more libraries available, but the set above was compiled by an attempt/error approach, which was indeed a tough task. You have to restart Glassfish in order to use those new libraries.

The next step is to create a connection pool and a JDBC resource, but I will assume that you know how to do that or you have read a post like <a href="http://blogs.sun.com/JagadishPrasath/entry/creating_jdbc_connection_pool_resource">the one written by Jagadish</a>.

Finally, you have to configure your persistence unit in order to use Hibernate. See parts of my persistence.xml file below:

{% highlight xml %}
<persistence version=”1.0″
  xmlns="http://java.sun.com/xml/ns/persistence"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://java.sun.com/xml/ns/persistence
       http://java.sun.com/xml/ns/persistence/persistence_1_0.xsd">
  <persistence-unit name="#persist-unit-name#" transaction-type="JTA">
    <provider>org.hibernate.ejb.HibernatePersistence</provider>
    <jta-data-source>#jdbc-datasource#</jta-data-source>
    <class>#persistence-class#</class>
      ... <!-- Your persistence classes -->
      <exclude-unlisted-classes>true</exclude-unlisted-classes>
      <properties>
        <property name="hibernate.dialect"
          value="org.hibernate.dialect.Oracle10gDialect"/>
        <property name="hibernate.show_sql" value="false"/>
        <property name="hibernate.cache.provider_class"
          value="org.hibernate.cache.HashtableCacheProvider"/>
      </properties>
    </persistence-unit>
  </persistence>
{% endhighlight %}

Basically, you have to set the provider tag with `org.hibernate.ejb.HibernatePersistence` and set some properties according to specific needs. That’s all!
