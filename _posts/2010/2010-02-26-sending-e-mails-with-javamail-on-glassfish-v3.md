---
layout: post
title: "Sending E-mails with JavaMail on Glassfish V3"
date: 2010-02-26 23:38:00 +0200
categories: enterprise application java java ee software architecture
---

One of the main advantages of using an application server like Glassfish is to keep your application free of complex code, such as 1) manual control of database transactions; 2) database access configuration; 3) security authentication and authorization; 4) sending and receiving e-mail messages, among many other complexities that are non-functional requirements, consuming the time we would be spending on functional requirements.

In my opinion, an important differential of <a href="http://glassfish.dev.java.net/">Glassfish V3</a> is its very rich and complete administration console. It is easy to use and to learn, which is, in my opinion, one of the most important competitive advantages, since it contributes to reduce the maintenance cost, a constant headache for system administrators. We are going to use the administrative console in order to configure a JavaMail resource for applications that aim to send emails</b>.

Follow the steps below:

1. enter in the administrative console (http://[server-name]:4848/)
2. go to _Resources / JavaMail Sessions_
3. create a new JavaMail session and set the following mandatory properties:
  - _JNDI Name_: mail/[email-account-name]
  - _Mail Host_: [smtp-server-address]
  - _Default User_: the username to authenticate on the smtp server
  - _Default Return Address_: the address used by recipients to reply the message. Some servers require that this address should be the one used by the authenticated user to access his mailbox.

If the server doesn’t request secure authentication, then the three steps above are enough to start using the new JavaMail session, but a server without secure authentication is a very rare case nowadays. You will certainly need to inform a password to login on the smtp server. In most cases, the server administrator also changes the default port of the smtp server, which forces us to explicitly inform the correct port. For these special needs we can use additional properties in the JavaMail session. Follow the steps below:

1. Still on the JavaMail session form, go to the _Additional Properties_ section and add 3 more properties, which are:
  - _mail.smtp.port_: [port-number]
  - _mail.smtp.auth_: true
  - _mail.smtp.password_: ******
2. Click on _Save_ to create the JavaMail session.

The last step is how to use this new JavaMail session in our applications to send emails. Using the JNDI name, we are going to inject the JavaMail session in a Java class, which could be a POJO of a pure web application, an EJB Session Bean, or any other type of class. See the code below for details:

{% highlight java %}
public class UserAccountBsn {

  @Resource(name = "mail/[email-account-name]")
  private Session mailSession;

  public void sendMessage(UserAccount userAccount) {
    Message msg = new MimeMessage(mailSession);
    try {
      msg.setSubject(“[app] Email Alert”);
      msg.setRecipient(RecipientType.TO,
        new InternetAddress(userAccount.getEmail(),
        userAccount.toString()));
      msg.setText(“Hello “+ userAccount.getName());
      Transport.send(msg);
    } catch(MessagingException me) {
      // manage exception
    } catch(UnsupportedEncodingException uee) {
      // manage exception
    }
  }
}
{% endhighlight %}

The @Resource annotation receives the JNDI name of the JavaMail session and injects an instance of the session in the variable _mailSession_. This variable is used within the _sendMessage_ method to create a new _MimeMessage_. The content of the message is built and finally sent to the recipient by the method _Transport.send_. The method receives as parameter an entity class representing an user registered on the application. It is so simple, isn’t it? 😉

Using this feature, we avoid any additional implementation to add those parameters hardcoded or parameterized, saving a lot of time, simplifying the maintenance of the applications, and reusing existing resources naturally shared by the container.
