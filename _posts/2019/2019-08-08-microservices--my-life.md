---
layout: post
title:  "The Microservices of My Life"
date: 2019-08-08 12:00:00 +0200
categories: microservices architecture design
---

![Brussels Airport](/images/posts/louvain-la-neuve-grand-place.jpg)

In August 2016, the rector of the [Université catholique de Louvain][uclouvain] was embarrassed. We was hosting a large event at the university and had to make an important decision: Let the portal up and running for the entire academic community to propagate the message he was disseminating at the event or let the students consult their grades of the second cycle of exams. He opted to frustrate the students. The months that followed were full of discussions about how to prevent this problem to happen again.

<!-- more -->

## Portal vs. Students

To load the page with the grades, the backend had to query data from 12 different tables. Every refresh of that page from every connected student would run those 12 queries over and over again. The more anxious the students were the worse the problem became. It wouldn't take too long to get the database overloaded and down. It was always a problem, but the increasing number of students made the implementation unsustainable.

![Students Enrollment](/images/posts/bureau-virtuel.jpg)

The solution we came up with was simple: still run those 12 queries in batch, dump the result in [JSON] documents, one for each student, and store them in a single table of a dedicated database. Two great improvements happened: those 12 queries are now running in sequence, not in parallel, reducing the concurrency cost, and the grades are available after a single query to a single table, indexed by the student id. The student could refresh that page as frequent as their anxiousness required and the page loaded instantly all the time. The pick was 30% of CPU time in the worse case. A cheap solution for the next decades.

## Scores Encoding

Working at the university also gave me the most rewarding project of my entire carrier: the outstanding gratitude of my users. Believe it of not, but up to 2016, all teachers, assistants and secretaries were busy encoding grades in paper forms. Teachers couldn't care less, but someone would have to encode all those tens of thousands grades from thousands of forms into the system, so the calculations would determine the future of each student.

![Students Enrollment](/images/posts/online_encoding.png)

Our mission was to balance the workload of the entire score encoding process. We had to release secretaries from the mountain of paper and repetitive tasks to spread the charge throughout the campus, delegating to teachers and their assistants the direct encoding into the system. Secretaries still had to review the data, but it was a breeze compared to previous years. After releasing the solution in production for a couple of days, a user reported a bug that we could not reproduce in our environment. So we decided to pay a visit to the user and observe how she was using the application. When the user announced our presence to her colleagues in them room each one of them came to thank for the job we have done. We even got a short round of applause. I will never forget this moment, but I hope to live it again.

## Online Enrollment

This image shocked me

![Students Enrollment](/images/posts/student-enrollment.jpg)

![Admission Form](/images/posts/admission-form.png)

## Internship Allocation

![Admission Form](/images/posts/internship-allocation.jpg)

## The Patterns

These are concise, domain specific, and technically advanced projects (for their respective times). They were developed apart from big monoliths applications as a factor of success. Nowadays, we have a nice name for them: **Microservices**, but we didn't call them that way. We simply called them **Applications**, and the fact that we spent time to do them right and future prof, they now fit into the concept of microservices.

They even follow some known microservices patterns, which are:
- _Database Per Service_: when you want to give a better life for your data, building a new home for them since you have the chance to improve the way they are treated.

- _Shared Database per Service_: when is ok for your data to live in community and all you want is to improve the way they are treated by building a more domain specific app.

- _Decompose by Domain_: It is not that your domains don't get along with each other. You just want them to not get mixed.

- _Strangler Pattern_: when you are afraid to change the monolith but you are fearless to disable it piece by piece as its features move to another app.

but the most interesting pattern is that every time we developed something detached from monoliths it was successful. So, you may disagree with the marketing around the word "microservices", but I would be happy if you at least think like a microservices person.

[JSON]: https://json.org
[uclouvain]: https://uclouvain.be
