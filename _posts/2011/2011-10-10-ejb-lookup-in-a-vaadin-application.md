---
layout: post
title: "EJB Lookup in a Vaadin Application"
date: 2011-10-10 09:16:00 +0200
categories: design patterns enterprise application java ee software architecture
---

It has been a long time since the last Service Locator I have implemented. I thought it wouldn’t be necessary anymore considering the maturity of the <a href="http://download.oracle.com/javaee/6/tutorial/doc/gjbnr.html">Java EE CDI</a> (Contexts and Dependency Injection). My first implementation was to make use of EJBs in a Struts-based web application. After that, I started working with JSF, which only requires annotated attributes with @EJB or @Resource to communicate with the business layer. So far, it has been a great experience until they asked me to evaluate <a href="http://www.vaadin.com/">Vaadin</a> as a front-end technology for business applications.

Before going too far, I have read the article “<a href="https://vaadin.com/wiki/-/wiki/Main/Adding%20JPA%20to%20the%20Address%20Book%20Demo">Adding JPA to the Address Book Demo</a>“, published on Vaadin’s wiki, which explains how to call EJBs from Vaadin’s classes to retrieve and persist data from the business layer. EJBs use JPA to get and put data in the database. They suggested to call EJBs from a custom servlet, which, according to the Java EE specification, has the ability to make EJB calls using CDI. If we have 1 or 3 EJBs to call, it seems to be an appropriate solution, but what to do in the Servlet when we have ~40 EJBs to deal with? How to pass all these references to Vaadin’s application class? The interface of this class can go nuts! That’s why I believe that the lookup using JNDI is desirable.

The following code is the Service Locator that I’m using in my Proof of Concept (PoC).

{% highlight java %}
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;

public class ClientServiceLocator {
  private Context initialContext;
  private Map<string, object=""> cache;
  private static ClientServiceLocator ourInstance =
      new ClientServiceLocator();

  public static ClientServiceLocator getInstance() {
    return ourInstance;
  }

  private ClientServiceLocator() {
    try {
      this.initialContext = new InitialContext();
      this.cache = Collections.synchronizedMap(
          new HashMap<string, object="">());
    } catch(NamingException ne) {
      System.err.printf(
          "Error in CTX looking up %s because of %s while %s",
          ne.getRemainingName(), 
          ne.getCause(),
          ne.getExplanation());
    }
  }

  public Object lookupEjb(String ejbName) {
    if(this.cache.containsKey(ejbName)) {
      return this.cache.get(ejbName);
    }
    else {
      try {
        Object ejbRef = initialContext.lookup("java:comp/env/"+ ejbName);
        this.cache.put(ejbName, ejbRef);
        return ejbRef;
      } catch (NamingException ne) {
        throw new RuntimeException(ne);
      } catch (Exception e) {
        throw new RuntimeException(e);
      }
    }
  }
}
{% endhighlight %}

The class `MyServiceLocator` follows the _Singleton_ design pattern, making sure that there is only one instance of the object to serve all requests from the web application. The unique instance is created at the class’ initialization process and since the constructor is private, the class cannot be instantiated by another class, being available only through the method `getInstance()`. The constructor initializes the context and creates a synchronized map where we store all references already created. The method `lookupEjb(String ejbName)` locates EJBs whose names are available in the local JNDI context. This method only works for those EJBs whose references are declared in the web.xml file, as listed below.

{% highlight xml %}
<web-app version=”2.5″
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns="http://java.sun.com/xml/ns/javaee"
    xsi:schemalocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd">

  <display-name>Information Systems</display-name>
  ...
  <ejb-local-ref>
    <ejb-ref-name>InformationSystemBean</ejb-ref-name>
    <ejb-ref-type>Session</ejb-ref-type>
    <local>example.business.InformationSystemBeanLocal</local>
    <ejb-link>eac-architecture-ejb.jar#InformationSystemBean</ejb-link>
  </ejb-local-ref>
</web-app>
{% endhighlight %}

The tag `<ejb-local-ref>` is used to declare a reference to a local EJB. The example above maps only one EJB. So, you have to repeat it for each EJB you want to map. Details about this tag can be found [here](http://download.oracle.com/docs/cd/E13222_01/wls/docs81/webapp/web_xml.html#1013984). Once declared, we can get an instance of the EJB in any part of the application using the following code:

{% highlight java %}
private InformationSystemLocal informationSystemBsn =
    (InformationSystemLocal)MyServiceLocator.getInstance()
        .lookupEjb("InformationSystemBean");
{% endhighlight %}

The variable is typed with the EJB local interface, which is `InformationSystemLocal`. The service locator returns an instance of the EJB named as `InformationSystemBean`, which is by default the EJB’s implementation class. Notice that none of the code above is necessary when we use CDI. The invocation of AjudaBsn would be simply like that:

{% highlight java %}
@EJB
private InformationSystemLocal informationSystemBsn;
{% endhighlight %}

CDI is good and elegant, but not widely applicable. The way it is implemented today is the main weakness of the Java EE specification. Maybe there is some strong reason why EJB’s annotations don’t work in every Java class. I simply don’t see this misterious reason because Spring has addressed this issue since long time ago simply using aspect orientation.
