---
layout: post
title: "The Importance of Software Modeling"
date: 2008-05-01 20:57:00 +0200
categories: uncategorized enterprise application java software architecture software engineering strategy
---

During my free time I made a very big refactoring of the Planexstrategy business layer. I transformed static business methods to EJB3 (Enterprise Java Beans version 3). All business classes are now stateless session beans and my entity classes are now mapped using JPA (Java Persistence API) to an Oracle database. Putting it in numbers, I converted 73 business classes to EJBs and I mapped 81 entity classes using JPA. I also had to update 270 references to business components in the control layer, fix a lot of bad code and retest the whole application. I spent at least two months to do everything.

Why did I make such madness? If I have to give a reason, just one is enough to justify: <span style="font-style: italic;">Business layer as static methods</span>. Yes, It is pretty ugly for an object-oriented implementation!  Anyway, it worked very well with a very good performance for, at least, 2 years. Other good reasons push me out to continue insistently:

<ol>
<li>EJB is finally easy to implement, maintain and test. Some people disagree about the “easy” adjective, but I assure it after 73 conversions. I had just to add the necessary annotations and make some changes in my business classes because they already look like EJBs, since I tried to simulate the stateless property using static methods. Now, any business method can be exposed as web services, the business layer can be accessed by different types of clients (web or desktop, locally or remotely) and a set of integration possibilities is now available to interchange data with systems of the organization or even outside it.</li>
<li>I hate to create a bizarre package .har to pack entity classes in JBoss. If you want to use Hibernate in an optimal way under JBoss, it’s necessary to put all your entity classes in a .har file, which is deployed within the .ear package. I definitely decided for JPA because I can still use Hibernate but in a standard way, without any explicit reference to the Hibernate library, which gives more portability to the application.</li>
<li>I love to think about the future and when I assume the risk of changing entire layers of an application it’s because I visualize it as part of a big scenario, where workflows will be even more automated, companies will not survive without a minimal level of integration with other companies, there is no programming language generic enough to address all technical issues and such languages should be integrated anyway, and many other things.</li>
</ol>
This was not my first experience with a big refactoring, but it was the most important in terms of knowledge and convictions. In other moments I will share this knowledge. Now I will talk about an important conviction that I had in the past and now it was weakened in my culture by agile methodologies: <span style="font-weight: bold;">the importance of software modeling as a requirement to implement software</span>. I will start the subject citing a Martin Fowler’s text:<br/><span style="font-size:85%;"></span>

> “The only checking we can do of UML-like diagrams is  peer review. While this is helpful it leads to errors in the design that are  often only uncovered during coding and testing. Even skilled designers, such as  I consider myself to be, are often surprised when we turn such a design into  software.”

Martin is an important agile guru. Anyone who wants to follow an agile methodology should read his ideas about the subject. I did that and I still believe in most of them, but during the Planexstrategy refactoring I learned how important is to see a global view of the implementation before implementing a new functionality. I will illustrate it using UML component models, however, I tried to simplify them in order to save time. When you see a direct link between components, actually you are seeing a link to an interface of the component, as illustrated by the figure below:

![component-model-correct.png](/images/posts/component-model-correct.png)

The text in the figure is in Portuguese, but it will not confuse your understanding about the problem. It isn’t necessary to explain what each element means. The component CotacaoProdutoBsn uses the component ProdutoBsn through its interface ProdutoLocal. This interface is used by the EJB container to make components available for clients running in the same application server. Because this interface should be defined for all components, I will assume it is present in all links between components and hide it from the component diagram.

After an extensive work to convert all business classes to EJB, I finally went to test the EJBs on the application server. I had to solve a lot of annotation mistakes and finally all error messages disappeared. However, just a subset of EJBs were started. No reasonable message was listed in the log to justify why many others EJBs just didn’t start as expected. I spent some days until I realized that there is no limitation on the number of EJBs, no memory leaks and no additional annotation mistakes, but a serious and dangerous high coupling between EJBs. The figure below illustrates the situation:

![component-model-wrong.png](/images/posts/component-model-wrong.png)

As you can see on the highlighted links, AtividadeBsn and TarefaBsn are interdependent and AtividadeBsn and UsoRecursoBsn are also interdependent. These were only two cases in a list of 20. Well, how something terrible like this can happen in a Java application developed by an expert programmer with years of experience? 😉

I should be humble and honest with myself to assume my mistake and publish it in my blog. At the same time, I can list some reasons for that:

- I received a lot of pressure from costumers to implement new features in a short period of time
- The runtime infrastructure is not robust enough to validate the application before a deployment process
- I don’t have a complete overview of the software components and it isn’t easy to detect a high coupling without a complete source code reading of other components.

Then, I realized that, if I had a component diagram like the figure below before starting to implement, that kind of mistake might have been avoided. Don’t you think?

![component-model-right.png](/images/posts/component-model-right.png)

In my opinion: yes. We can visualize if it’s necessary to add new components or just increment an existent one, reuse existent implementations from other components and remember that AtividadeBsn should not invoke a TarefaBsn method and neither should UsoRecursoBsn be aware of the existence of AtividadeBsn.

Finally, contrary to some agile practices, UML diagrams should be strongly considered and it should be drawn using a software instead of sketches in a piece of paper, since we have to update such diagrams all the time. If you disagree with my position, please tell me if I can avoid high coupling mistakes without UML diagrams.
