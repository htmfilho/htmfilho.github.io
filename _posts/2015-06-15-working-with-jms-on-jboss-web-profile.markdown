---
layout: post
title: "Working With JMS on JBoss Web Profile"
date: 2015-06-15 18:43:46 +0200
categories: development enterprise application integration javaee jms software architecture
---

If you didn’t get in contact with messaging systems yet you better do it soon. This concept is a key element in the architecture of scalable applications. Before it was a product but now it’s pervasive even natively embedded in some programming languages.

Let me help you to use messaging in a JavaEE application server. The Java application code is portable between application servers. Unfortunately, each application server has its own way to configure a messaging system. Since I can’t cover all of them, I will concentrate on JBoss 7 or superior (JavaEE 6/7). JBoss uses a messaging system called <a href="http://hornetq.jboss.org" target="_blank">HornetQ</a>, an open source message-oriented middleware. It offers queues (point-to-point) and topics (publisher-subscriber). I’m covering only queues in this post. Queues and topics can be used within a JavaEE application or across several applications. It’s a kind of integration pattern, but sadly less popular than web services. Since I’m not dealing with integration, I will narrow even more this post to cover a queue accessible locally only.

<a href="http://www.hildeberto.com/wp-content/uploads/2015/06/metro-crowd.jpg">![metro-crowd.jpg](/images/posts/metro-crowd.jpg)</a>

I recently had to use a queue to asynchronously generate large files. Users were waiting too much for a response from the server after requesting those large files. The problem became serious when multiple users were doing that request simultaneously. By using a queue, I was able to generate files asynchronously, so the users didn’t have to wait anymore, and in sequence, avoiding exponential use of memory and IO.

To put some pepper on the issue, we were using JBoss Web Profile and it doesn’t support messaging. We would need to migrate to JBoss Full Profile, but it would require us to migrate all development machines and all server environments, otherwise the deployment descriptor with the queue configuration would break the deployment everywhere. Also, migrating to the full profile would bring together several additional services – that we don’t need at all – just to consume more resources. So, I had to figure out how to make the messaging system work in the web profile.

The first idea that came to my mind was to simply identify the messaging configuration in the full profile (standalone-full.xml) and copy it to the web profile (standalone.xml). I started by adding the extension module:

```
<extensions>
...
<extension module="org.jboss.as.messaging"/>
...
</extensions>
```

and with it comes its respective rather long subsystem:

```
<subsystem xmlns="urn:jboss:domain:messaging:1.4">
  <hornetq-server>
    <persistence-enabled>true</persistence-enabled>
    <journal-type>NIO</journal-type>
    <journal-min-files>2</journal-min-files>
    <connectors>
      <netty-connector name="netty" socket-binding="messaging"/>
      <netty-connector name="netty-throughput" 
            socket-binding="messaging-throughput">
        <param key="batch-delay" value="50"/>
      </netty-connector>
      <in-vm-connector name="in-vm" server-id="0"/>
    </connectors>
    <acceptors>
      <netty-acceptor name="netty" socket-binding="messaging"/>
      <netty-acceptor name="netty-throughput"
            socket-binding="messaging-throughput">
        <param key="batch-delay" value="50"/>
        <param key="direct-deliver" value="false"/>
      </netty-acceptor>
      <in-vm-acceptor name="in-vm" server-id="0"/>
    </acceptors>
    <security-settings>
      <security-setting match="#">
        <permission type="send" roles="guest"/>
        <permission type="consume" roles="guest"/>
        <permission type="createNonDurableQueue" roles="guest"/>
        <permission type="deleteNonDurableQueue" roles="guest"/>
      </security-setting>
    </security-settings>
    <address-settings>
      <address-setting match="#">
        <dead-letter-address>jms.queue.DLQ</dead-letter-address>
        <expiry-address>jms.queue.ExpiryQueue</expiry-address>
        <redelivery-delay>0</redelivery-delay>
        <max-size-bytes>10485760</max-size-bytes>
        <page-size-bytes>2097152</page-size-bytes>
        <address-full-policy>PAGE</address-full-policy>
        <message-counter-history-day-limit>
            10
        </message-counter-history-day-limit>
      </address-setting>
    </address-settings>
    <jms-connection-factories>
      <connection-factory name="InVmConnectionFactory">
        <connectors>
          <connector-ref connector-name="in-vm"/>
        </connectors>
        <entries>
          <entry name="java:/ConnectionFactory"/>
        </entries>
      </connection-factory>
      <connection-factory name="RemoteConnectionFactory">
        <connectors>
          <connector-ref connector-name="netty"/>
        </connectors>
        <entries>
          <entry name="java:jboss/exported/jms/RemoteConnectionFactory"/>
        </entries>
      </connection-factory>
      <pooled-connection-factory name="hornetq-ra">
        <transaction mode="xa"/>
        <connectors>
          <connector-ref connector-name="in-vm"/>
        </connectors>
        <entries>
          <entry name="java:/JmsXA"/>
        </entries>
      </pooled-connection-factory>
    </jms-connection-factories>
    <jms-destinations>
      <jms-queue name="ExpiryQueue">
        <entry name="java:/jms/queue/ExpiryQueue"/>
      </jms-queue>
      <jms-queue name="DLQ">
        <entry name="java:/jms/queue/DLQ"/>
      </jms-queue>
    </jms-destinations>
  </hornetq-server>
</subsystem>
```

No changes from the original. I just copied and pasted the entire messaging subsystem. Then I added a socket binding just in case I needed queues and topics for integration purposes later on:

```
<socket-binding-group
   name="standard-sockets"
   default-interface="public"
   port-offset="${jboss.socket.binding.port-offset:0}">
  ...
  <socket-binding name="messaging" port="5445"/>
  <socket-binding name="messaging-group"
     port="0"
     multicast-address="${jboss.messaging.group.address:231.7.7.7}"
     multicast-port="${jboss.messaging.group.port:9876}"/>
  <socket-binding name="messaging-throughput" port="5455"/>
  ...
</socket-binding-group>
```

Finally, I added a reference to the resource adapter, defined above, in the EJB subsystem, as follows:

```
<subsystem xmlns="urn:jboss:domain:ejb3:1.4">
  ...
  <mdb>
    <resource-adapter-ref
       resource-adapter-name="${ejb.resource-adapter-name:hornetq-ra}"/>
    <bean-instance-pool-ref pool-name="mdb-strict-max-pool"/>
  </mdb>
  ...
</subsystem>
```

And it worked! Be aware you can simply use the full profile to make the messaging work. No need to do all this configuration. But keep in mind that the full profile is going to load additional things you don’t need at all, such as:

<ul>
<li><strong>org.jboss.as.cmp</strong>: container-managed persistence, deprecated in favour of JPA.</li>
<li><strong>org.jboss.as.jacorb</strong>: an implementation of CORBA.</li>
<li><strong>org.jboss.as.jsr77</strong>: abstracts manageable aspects of the J2EE architecture to provide a model for implementing instrumentation and information access.</li>
</ul>
<a href="http://www.hildeberto.com/wp-content/uploads/2015/06/metro-queue.jpg">![metro-queue-1024x768.jpg](/images/posts/metro-queue-1024x768.jpg)</a>

On the application side I did three things:

1 – add the deployment descriptor hornetq-jms.xml to the folder WEB-INF to automatically create a queue during the deployment process. The descriptor has the following content:

```
<?xml version="1.0" encoding="UTF-8"?>
<messaging-deployment xmlns="urn:jboss:messaging-deployment:1.0">
  <hornetq-server>
    <jms-destinations>
      <jms-queue name="FileGenerationQueue">
        <entry name="/queue/FileGeneration"/>
      </jms-queue>
    </jms-destinations>
  </hornetq-server>
</messaging-deployment>
```

2 – create a MDB (Message-Driven Bean) to listen to the queue and process the messages as they arrive. For example:

```
@MessageDriven(name="FileGenerationQueue", activationConfig = {
     @ActivationConfigProperty(propertyName = "destination",
                               propertyValue = "queue/FileGeneration"),
     @ActivationConfigProperty(propertyName = "destinationType",
                               propertyValue = "javax.jms.Queue"),
     @ActivationConfigProperty(propertyName = "acknowledgeMode",
                               propertyValue = "Auto-acknowledge")})
public class LargeFileGenerationBean implements javax.jms.MessageListener {
  @Override
  public void onMessage(Message message) {
    // Code that will process messages coming from the queue.
  }
}
```

3 – and modify a Request Scoped Managed Bean to send messages to the queue. For example:

```

@ManagedBean
@RequestScoped
public class MyManagedBean implements Serializable {

  @Resource(mappedName="java:/ConnectionFactory")
  private ConnectionFactory connectionFactory;

  @Resource(mappedName="java:/queue/FileGeneration")
  private Queue queue;

  // Serializable class encapsulating data criteria.
  private DataCriteria dc;

  public String sendMessageToQueue(String message) {
    try (Connection connection = connectionFactory.createConnection()) {
      Session session = conn.createSession(false,
      Session.AUTO_ACKNOWLEDGE);
      MessageProducer producer = session.createProducer(queue);
      conn.start();

      ObjectMessage message = session.createObjectMessage(dc);
      producer.send(message);
    } catch (JMSException e) {
      ...
    }
  }
}
```

Let me know if you have any issues, then we can find the solution and make it better.
