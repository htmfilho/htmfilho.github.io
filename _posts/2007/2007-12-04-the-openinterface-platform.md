---
layout: post
title: "The OpenInterface Platform"
date: 2007-12-04 10:17:00 +0200
categories: research
---

![OpenInterface](/images/posts/2007-12-04-the-openinterface-platform.png)

In the last few months, I’ve been dedicating some time to collaborate with the OpenInterface platform, an open source project conceived to integrate components developed in different programming languages. But, why am I so interested on it? Basically, because it is part (not the main issue) of my research in multi modalities and because it is a project managed by people in my laboratory at Université catholique de Louvain.

The OpenInterface was conceived to support the development of multi modal applications. It is developed in C++ because of the team’s expertise and for performance reasons. Its architecture is centered in a kernel, which intermediates the conversation between components. There is a proxy for each programming language able to invoke the component, send and receive data from it. Finally, the components are installed in the platform to be visible by other components.

It is true that you can use OpenInterface for different proposals. Actually, it is very attractive for software integration, but its focus is to work with components that implement any user interaction modality, like speech recognition, gesture recognition and so on. This focus was fixed because of the context where the platform was conceived: in a laboratory of signal processing, where exists a high volume of data processing but nobody cares if you will store the data in a database or interact with a message queue (there is no concern about transactions). The important aspect of the multi modal interaction domain is time. The volume of data is higher but not sensible enough to be reproved by small inconsistencies (detected by pattern recognition and other heavy strategies).

The platform has gained popularity nowadays because of many contributions of the community, who developed a rich set of components to improve the user interaction. Some cool components are: [Simple Posture Recognition](http://www.openinterface.org/platform/project/posturerec), [Simple Image Navigator](http://www.openinterface.org/platform/project/navigationtoy), [5DT Data Glove](http://www.openinterface.org/platform/project/gloves5dt) and others. A [complete list](http://www.openinterface.org/platform/component_database) is available in the OpenInterface platform [website](http://www.openinterface.org/platform/).

But, OpenInterface is not only a software platform. Actually, a complete environment was created around it. As you can see in the [homepage of the OpenInterface website](http://www.openinterface.org), there are 4 different and complementary initiatives, which are:

- **OpenInterface Platform**: it is what we discussed above. A framework to develop multi modal applications rapidly.

- **OpenInterface Foundation**: It is a non-profit organization to coordinate, expand and integrate activities of many people around the world involved in the field of multi modal interface research. One of the most important initiatives of the foundation was to create the [Journal on Multimodal User Interfaces](http://www.jmui.org).

- **OpenInterface Forge**: The source code of the OpenInterface Platform and all available contributions is available for free in the Forge website, which manages all contributions as open source projects.

- **OpenInterface Strep**: finally, this project is focused on the platform improvements and its integration with the industry.

If you want to evaluate or apply OpenInterface in your project, visit [OpenInterface Forge website](http://forge.openinterface.org) and get the binary distribution and other contributions. You can register and be involved in the project as a contributor. Assign to the mailing list of what you want to use and ask for help when necessary.
