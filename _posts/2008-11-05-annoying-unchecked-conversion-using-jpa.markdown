---
layout: post
title: "Annoying Unchecked Conversion using JPA"
date: 2008-11-05 08:07:00 +0200
categories: uncategorized database enterprise application ide java jvm netbeans
---

I’m a great user of the Java Persistence API (JPA). It just simplifies the code a lot when interacting with databases. Even with the simplification, the code keeps its readability because the API is object-oriented, very close to our mental abstraction. However, it is still very criticized because of pending features like Criteria, a better default implementation (Toplink sucks!) and a consistent implementation considering Generics. Actually, the last one is the reason of this post, which describes an insignificant but annoying experience with unchecked conversion caused by a weak support of Generics.

The code below shows a business method in a stateless session beans that returns a list of Transcription’s instances created by the JPA with data retrieved from the database.

<pre style="font-size:83%; font-family: courier new;">public List<transcription> findTranscriptions(Segment segment) {<br/>Query query em.createQuery("select t from Transcription t <br/>where t.segment = :segment");<br/>query.setParameter("segment", segment);<br/>return query.getResultList();<br/>}<br/></transcription>
```

When we implement this method using Netbeans, no warning message appears automatically. It might not occur because the editor doesn’t understand the word “Transcription” in the query as an entity class. However, the warning message below appears if we put the additional parameter <span style="font-style:italic;">-Xlint:unchecked</span>, which tells the compiler to give more detail for unchecked conversion warnings.

<pre style="font-size:83%; font-family: courier new;"><...>/AnnotationServiceBean.java:70: warning:<br/>[unchecked] unchecked conversion<br/>found   : java.util.List<br/>required: java.util.List<...entity.Transcription><br/>.getResultList();<br/>1 warning<br/>
```

According to <a href="http://java.sun.com/mailers/techtips/enterprise/2007/TechTips_April07.html">this</a> document, created by Sean Brydon at Sun Microsystems, the warning is generated because query.getResultList() returns a non-generic version of List, when the return type expects “List<transcription>“. To stop the warning, we are obliged to add the annotation <span style="font-style:italic;">@SuppressWarnings(“unchecked”)</span> just before the method declaration as shown below.</transcription>

<pre style="font-size:83%; font-family: courier new;">@SuppressWarnings("unchecked")<br/>public List<transcription> findTranscriptions(Segment segment) {<br/>Query query em.createQuery("select t from Transcription t <br/>where t.segment = :segment");<br/>query.setParameter("segment", segment);<br/>return query.getResultList();<br/>}<br/></transcription>
```

The same document mentions that in a future version of the Java Persistence API, the <span style="font-style:italic;">javax.persistence.Query</span> class will likely change to better support generics. This post is to stimulate them to do it faster, because for me <span style="font-style:italic;">@SuppressWarnings(“unchecked”)</span> is actually a dirt in my beautiful and legible source code.
