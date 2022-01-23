---
layout: post
title: "Choosing Between Vaadin and JSF"
date: 2012-01-31 16:01:00 +0200
categories: browser java jsf open source software architecture user interface web
---

With the recent release of [Primefaces 3.0](http://blog.primefaces.org/?p=1588), JSF finally reaches an unprecedent level of maturity and utility that puts it face to face with other popular Rich Internet Applications (RIA) options, such as Google Web Toolkit (GWT), ExtJS, Vaadin, Flex and others. This open source project also proved to be very active and in a constant growing path.

I have been working with JSF + Primefaces since October 2010, when I started developing the project JUG Management, a web application conceived to manage user groups or communities focused on a certain domain of knowledge, whose members are constantly sharing information and attending social and educational events. [JSF](http://www.oracle.com/technetwork/java/javaee/javaserverfaces-139869.html) is a standard Java framework for building user interfaces for web applications with well-established development patterns and built upon the experience of many preexisting Java Web development frameworks. It is component-based and server-side user interface rendering, sending to clients (web browsers) pre-processed web based content such as HTML, JavaScript and CSS. My experience on this technology is openly available on [java.net](http://java.net/projects/cejug/sources/jug-management/show).

Meanwhile, I had the opportunity to create a Proof of Concept (PoC) to compare JSF and Vaadin in order to help developers and architects to decide between one of them. Vaadin is a web application framework for RIA that offers robust server-side architecture, in contrast to other Javascript libraries and browser plugin-based solutions. The business logic runs on the server while a richer user interface, based on Google Web Toolkit (GWT), is fully rendered by the web browser, ensuring a fluent user experience.

The result of the PoC was surprisingly interesting 🙂 It ended up proposing both technologies instead of eliminating one of them. I found out, exploring available books, articles, blogs and websites, that despite being able to implement all sorts of web applications, each technology has special characteristics, optimized to certain kinds of those applications. In practical terms, if we find out that JSF is better for a certain kind of application, that’s because it would take more time and code to do the same with Vaadin. The inverse logic is also true. In order to understand that, we have to visit two fundamental concepts that have direct impact on web applications:

- [**Context of Use**](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.100.4512) considers the **user** who will operate the application, the **environment** where the user is inserted, and the **device** the user is interacting with.
- [**Information Architecture**](http://shop.oreilly.com/product/9780596000356.do) considers the **user** of the application again, the **business domain** in which he or she works on and the **content** managed in that domain.

Notice in the figure bellow that the user is always the center of attention in both concepts. That’s because we are evaluating two frameworks that have direct impact on the way users interact with web applications.

![context-use-information-architecture.png](/images/posts/context-use-information-architecture.png)

Visiting the concepts above we have:

**<span style="color: #3d85c6; font-size: large;">Environment</span>**<br/>Some applications are available for internal purpose only, such as the ones available on the intranet, other applications are used by external users, such as the company website.

Users of internal applications are more homogeneous and in limited number, which means that the UI can be a bit more complex to allow faster user interactions. That explains the fight Microsoft Office vs. Google Docs. The last one is not yet fully acceptable in the office environment because it has less functionalities than Microsoft Office. The latter is, on the other hand, more complex and more expensive. However, a limited number of users to a larger number of features makes acceptable to have some additional costs with training sessions to profit from the productivity features.

A company website targets heterogeneous users in unlimited environments. It is not possible to train all this people, thus simpler user interfaces with short and self-explanatory interactions are desirable.

**Considering the environment, we would recommend Vaadin for homogeneous users in limited environments and JSF for heterogeneous users in unlimited environments.**

**<span style="background-color: white; color: #3d85c6; font-size: large;">Device</span>**<br/>Different devices demand multiple sets of UI components, designed to look great from small to large screens. Fortunately, both frameworks have components to support the full range of screen sizes from regular desktops to mobile devices. The problem is that different devices bring different connectivity capabilities and the application should be ready to deal with short band-width and reduced transfer rates. In this case, **Vaadin seems to be more suitable for multiple devices, as long as the variety of devices is not so extensive, because the user interface is rendered locally, using JavaScript, and it has a richer Ajax support to optimize the exchange of application data with the server.**

**<span style="color: #3d85c6; font-size: large;">Business Domain</span>**<br/>In principle, good quality UI frameworks such as JSF and Vaadin can implement any business domain. The problem is how experienced the team is with the technology or how small is the learning curve to master it. Business is about timing and the technology that offers the best productivity will certainly win. **If your team has previous experience with Swing then Vaadin is the natural choice. If the previous experience was more web-oriented, manipulating HTML, CSS ans Scripts, then JSF is recommended.**

**<span style="color: #3d85c6; font-size: large;">Content</span>**<br/>Content is a very relevant criterion for choosing between Vaadin and JSF. **In case the application needs to deal with volumous content of any type, such as long textual descriptions, videos, presentations, animations, graphics, charts and so on, then JSF is the recommended over Vaadin because JSF uses a web content rendering strategy to profit from all content-types supported by web browsers without the need for additional plugins or tags**. The support for multiple content is only available on Vaadin through the use of plugins, which must be individually assessed before adoption.

<span style="background-color: white; color: #3d85c6; font-size: large;">**User**</span><br/>Last, but not least, we have the user, who is the most important criterion when choosing a UI framework. We would emphasize two aspects:

1. **The user population**: the largest is the target population the highest are the concerns about application compatibility. It must deal with several versions and types of browsers, operating systems, computers with different memory capacity and monitor resolution. All these without failures or security issues. **For larger populations, the most appropriate technology is the most compatible one in a cross-platform environment, which is the case of JSF, since it uses a balanced combination of HTML, JavaScript and CSS, while Vaadin relies only on JavaScript and CSS. But shorter populations would have better profit with Vaadin** because cross-browser compatibility is and will remain being a very hard work to be done by Vaadin’s development team behind the scene.

2. **User’s tasks**: If the application is intensively operated by users then it is expected that it has more user’s tasks implemented. On the other hand, if the application is rarely used or has short intervals of intensive use, then there is a lower concentration of user’s tasks. According to the PoC, **Vaadin is the technology that provides the best support on delivering user tasks with richer user interaction because of its fast visual response. JSF is less optimized on which concerns the user interaction**.

In conclusion, instead of discarding one of these frameworks consider both on the shelf of the company’s architectural choices, but visit the criteria above to make sure that you are using the right technology to implement the expected solution. A simple way to apply those criteria would be to assign weights to each criterion, according to the project’s characteristics; set which technology is appropriate for each criterion; and sum the weights for each technology. The highest weight elects the technology to be used in the project.
