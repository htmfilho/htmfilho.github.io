---
layout: post
title: "My Personal Software Development Process"
date: 2018-01-14 12:00:00 +0200
categories: documentation process agile development
excerpt_separator: <!--more-->
---

Unless you ask me to work in a different way to fulfil your business 
requirements, I'm going to perform the following process to develop applications
for you.

#### Create an issue for every single request

The smaller the granularity the easier it is to manage. It can be done and
released fast. It is initially put in the backlog.

#### Order the issues in descending order of priority

I organize the issues in descending order of priority. This way, the most
important issues are always visible. Unless there is a technical constraint, it
is the user who defines the priority.

#### Distribute the issues into releases

The frequence of releases is agreed with the users. The minimal frequence is one
week and the maximum is one month.

#### Update the user manual

In case of a new feature, I create a mockup and describe how it is going to work
in the user manual. Then I publish a draft version to enable consultation. If
the feature is not so trivial, I ask the users for their feedback. In case of
changing an existing functionality, I just change the text, not the images, because I'm going to replace the mockup or the outdated screenshot in a later
stage.

The modification in the user manual should be limited to the scope of the issue
that I'm working on.

> Every time I ask for a feedback of the user I also give an assumption and
deadline. If the feedback is not given until the deadline, the assumption is
considered as true, so the project can move forward without further delays.

#### Write test, pass test, refactor, repeat

To have the discipline of documenting before developing, I also have to have the
discipline of following TDD (Test-Driven Development) while developing. These 
are similar principle: I'm testing earlier so I'm actually testing everything, I'm documenting earlier so I'm actually documenting everything.

#### Take a screenshot of the change

The screenshot is used to replace the mockup or the outdated screenshot in the
user manual.

