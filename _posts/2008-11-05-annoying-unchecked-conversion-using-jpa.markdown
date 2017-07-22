---
layout: post
title: "Annoying Unchecked Conversion using JPA"
date: 2008-11-05 08:07:00 +0200
categories: database jpa java jvm netbeans
---

I’m a great user of the Java Persistence API (JPA). It just simplifies the code a lot when interacting with databases. Even with the simplification, the code keeps its readability because the API is object-oriented, very close to our mental abstraction. However, it is still very criticized because of pending features like Criteria, a better default implementation (Toplink sucks!) and a consistent implementation considering Generics. Actually, the last one is the reason of this post, which describes an insignificant but annoying experience with unchecked conversion caused by a weak support of Generics.

The code below shows a business method in a stateless session beans that returns a list of Transcription’s instances created by the JPA with data retrieved from the database.

{% highlight java %}
public List<Transcription> findTranscriptions(Segment segment) {
  Query query em.createQuery("select t from Transcription t where t.segment = :segment");
  query.setParameter("segment", segment);
  return query.getResultList();
}
{% endhighlight %}

When we implement this method using Netbeans, no warning message appears automatically. It might not occur because the editor doesn’t understand the word `Transcription` in the query as an entity class. However, the warning message below appears if we put the additional parameter `-Xlint:unchecked`, which tells the compiler to give more detail for unchecked conversion warnings.

```
<...>/AnnotationServiceBean.java:70: warning:
[unchecked] unchecked conversion
found   : java.util.List
required: java.util.List<...entity.Transcription>
.getResultList();
1 warning
```

According to [this](http://java.sun.com/mailers/techtips/enterprise/2007/TechTips_April07.html) document, created by Sean Brydon at Sun Microsystems, the warning is generated because `query.getResultList()` returns a non-generic version of List, when the return type expects `List<transcription>`. To stop the warning, we are obliged to add the annotation `@SuppressWarnings(“unchecked”)` just before the method declaration as shown below.

{% highlight java %}
@SuppressWarnings("unchecked")
public List findTranscriptions(Segment segment) {
  Query query em.createQuery("select t from Transcription t where t.segment = :segment");
  query.setParameter("segment", segment);
  return query.getResultList();
}
{% endhighlight %}

The same document mentions that in a future version of the Java Persistence API, the `javax.persistence.Query` class will likely change to better support generics. This post is to stimulate them to do it faster, because for me `@SuppressWarnings(“unchecked”)` is actually a dirt in my beautiful and legible source code.
