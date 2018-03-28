---
layout: post
title: "Discussion about Context during the UCVP Workshop"
date: 2009-11-07 01:54:00 +0200
categories: conference research
---

The 4th and 5th days of the ICMI-MLMI 2009 was dedicated to thematic workshops. On the 4th day I attended the <a href="http://hmi.ewi.utwente.nl/ucvp09">Workshop on Use of Context in Vision Processing</a> (UCVP), which was an opportunity for observing recent works on employing contextual information in problems of <a href="http://en.wikipedia.org/wiki/Computer_vision">Computer Vision</a>. There were very good talks all over the day, but what really interested me was a half-hour discussion about “Context” at the end of the workshop.

![DSC02571-300x225.jpg](/images/posts/DSC02571-300x225.jpg)
<div style="text-align: center;"><i>UCVP workshop venue</i></div>

At the second floor of the MIT Media Lab, we were freely discussing about why context is important and how it can improve computer vision. The point about context is that if you don’t have one, then either your problem is really big or you can solve many problems with a single solution. So, people are used to define a context in order to get results, which is a primary concern of financed research projects, where most of us are allocated on. The independence of context usually comes from attempts to reuse results from previous context-aware works on new projects focused on new contexts. Gradually, the original research becomes more and more generic until it achieves a balanced level of acceptance.

Let me give you an example of a context-aware (context-dependent) research. The work of Stefanie Tellex and Deb Roy, entitled “Grounding Spatial Prepositions for Video Search”, was presented during the conference and it considers a database of videos, recorded with a fish eyes camera, showing the routine of a family in a kitchen during some months. They track people and also record what they say to perform a set of experiments. Of course, the experiments are all related to people moving and talking in the kitchen. If they change to a different environment, like a meeting room, the results would change considerably. They cannot even guarantee that their current implementation will work in a different environment. It could be evaluated in other projects and some adjustments on the direction of generalization could be necessary, but still keeping the compatibility with the previous context.

![DSC02533-1-300x247.jpg](/images/posts/DSC02533-1-300x247.jpg)
<div style="text-align: center;"><i>Demo of the domestic surveillance database</i></div>

Now, an example of a context-unaware (context-independent) research. Antonio Torralba, Rob Fergus, and William T. Freeman have been working on the <a href="http://people.csail.mit.edu/torralba/tinyimages/">LabelMe</a> project, a large database of images, with around 80 million tiny images randomly found on the internet. Anyone visiting the LabelMe website can select objects that they recognize and label it with the name of the object. It helps to improve the performance of object recognition algorithms independent of the context. So, they are not studying a specific kind of context, but creating a general solution for several situations of object recognition.

![80-million-tiny-images-300x175.png](/images/posts/80-million-tiny-images-300x175.png)

<div style="text-align: center;"><i>Website of the </i><a href="http://people.csail.mit.edu/torralba/tinyimages/"><i>LabelMe</i></a><i> project</i></div>
What is still confusing for me is that sometimes people mix (or I mix) context and domain. For me, these are two different things, not totally different but differentiable. To make my point clear, let me describe a situation: Imagine a meeting room in a company where directors talk about the strategy of the company. When people go to a meeting at this room we have a contextual situation going on. All concepts within this situation are part of the domain too. But, what about the subjects people are discussing during the meeting? Is it part of the context or is it exclusively part of the domain?

According to the <a href="http://wordnet.princeton.edu/">WordNet database</a>, <b><i>context</i></b> is a set of facts or circumstances that surround a situation or event; and <b><i>domain </i></b>is the content of a particular field of knowledge. Domain seems to embrace context in the sense that it can describe the whole context. According to these definitions, what people talk at the moment is part of the context, but all subjects that people can possibly talk about their business are part of the domain, which should also be considered on the scientific experiments.

So, going back to context-awareness and context-unawareness, are we talking about context or domain? Is it context-aware or domain-aware? Context-unaware or domain-unaware? I never heard of domain-awareness/unawareness, but a lot of context-aware/unaware. How can we keep using the term “context” and still consider what people know but not necessarily say? Open question. Let’s think about it 😉
