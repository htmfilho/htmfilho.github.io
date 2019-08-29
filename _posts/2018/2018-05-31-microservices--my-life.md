---
layout: post
title:  "The Microservices of My Life"
date: 2018-05-31 12:00:00 +0200
categories: microservices architecture design
---

![Brussels Airport](/images/posts/louvain-la-neuve-grand-place.jpg)

In August 2016, the Dean of the [Université catholique de Louvain][uclouvain] was embarrassed. He was hosting a large event at the university and had to make an important decision: Let the portal up and running for the entire academic community to propagate the message he was disseminating at the event or let the students consult the grades of the second cycle of exams. He opted to frustrate the students. The months that followed were full of discussions about how to prevent this problem to happen again.

<!-- more -->

## Portal vs. Students

To load the page with the grades, the backend had to query data from 12 different tables. Every refresh of that page by every connected student would run those 12 queries over and over again. The more anxious the students were the worse the problem became. It wouldn't take too long to get the database overloaded and down. It was always a problem, but the increasing number of students made the implementation unsustainable.

![Students Enrollment](/images/posts/bureau-virtuel.jpg)

The solution we came up with was simple: still run those 12 queries in batch, dump the result in [JSON] documents, one for each student, and store them in a single table of a dedicated database. Two great improvements happened: those 12 queries are now running in sequence, not in parallel, reducing the concurrency cost, and the grades are available after a single query to a single table, indexed by the student's id. They could refresh that page as frequent as their anxiousness required and the page loaded instantly all the time. The peak was 30% of CPU time in the worse scenario. A cheap solution for the next decades.

## Scores Encoding

Working at the university also gave me the most rewarding project of my entire carrier: the outstanding gratitude of my users. Believe it or not, but up to 2016, all teachers, assistants and secretaries were busy encoding grades in paper forms. Teachers couldn't care less, but someone would have to encode all those tens of thousands grades from thousands of forms into the system, so the calculations would determine the future of each student.

![Students Enrollment](/images/posts/online_encoding.png)

Our mission was to balance the workload of the entire score encoding process. We had to release secretaries from the mountain of paper and repetitive tasks to spread the charge throughout the campus, delegating to teachers and their assistants the encoding into the system. Secretaries still had to review the data, but it was a breeze compared to previous years. After releasing the solution in production, a user reported a bug that we could not reproduce in our environments. So we decided to pay a visit to the user and observe how she was using the application. When the user announced our presence to her colleagues in them room each one of them came to thank for the job we had done. We even got a short round of applause. I will never forget this moment, but I hope to live it again.

## Online Registration

This image shocked me in 2014. If you look at it carefully, you will see the red sign "Inscriptions" in the entrance of the building. That building is big, thus when you see a queue like this outside that's because there is an even bigger queue inside. These people are trying to become students of the university. How many organizations out there have the privilege of getting so many people interested in their products or services? That university is in this select group, but they were not treating their "clients" well. So, when they gave us the opportunity to get those people registered online, I embarrassed the project like a son.

![Students Enrollment](/images/posts/student-enrollment.jpg)

Instead of increasing the monolith problem, we built an application dedicated to online registrations. Over several iterations, it covered all kinds of registrations and eliminated that queue forever. It also helped to eliminate the existing primitive module in the monolith.

![Admission Form](/images/posts/admission-form.png)

Curiously, all the above projects helped to improve the monolith. They eliminated all the existing performance issues since the load was shared among several smaller apps. It got extra life, reducing the pressure to replace it in a hurry and buying us time to do it properly.

## Internship Allocation

My latest mission as a team lead there was the recovery of an almost dead project. The Medical School was in need for a solution to assign students to internships in hospitals throughout the country (yes, Belgium is really small) and someone convinced them they could do it themselves with the help of some students. Needless to say that it was a disaster. The application was designed to run a single round of internships. It wasn't ready for the next academic year unless you cleaned up the database and started all over again.

When I realized that Medical School was feeling cheated, I gave a step ahead and proposed to my boss to assign the project to me since my team was already fully autonomous. I spent 2 months focused on that application and got it in good shape to all upcoming cohorts. Since I was leaving, I also spent some days training someone to continue my work.

![Admission Form](/images/posts/internship-allocation.jpg)

During this project I realized that's not a good idea to work alone. I had a lot of decision power, but nobody to challenge me. Therefore, it was the last time I played the hero. Fortunately, the person that took charge got what needed to be improved and I could leave in peace.

## The Patterns

These are concise, domain specific, and technically advanced projects. Being developed apart from big monoliths applications was a factor of success. Nowadays, we have a nice name for them: **Microservices**, but we didn't call them that way at the time. We simply called them **Applications**, and the fact that we spent time doing them right and future proof, they now fit into the concept of microservices. They even follow some [known patterns][patterns], which are:

- _Database Per Service_: when you want to give a better life for your data, building a new home for them since you have the chance to improve the way they are treated.

- _Shared Database per Service_: when is ok for your data to live in community and all you want is to improve the way they are treated by building a more domain specific app.

- _Decompose by Domain_: It is not that your domains don't get along with each other. You just want them to not get mixed.

- _Strangler Pattern_: when you are afraid to change the monolith but you are fearless to disable it piece by piece as its features move to other apps.

But the most interesting pattern is that every time we developed something detached from monoliths it was successful. So, you may disagree with the marketing around the word "microservices", but I would be happy if at least you think like a microservices expert, making small apps instead of big ones.

Many thanks to all the people I had the privilege of working with along this journey.

[JSON]: https://json.org
[patterns]: https://github.com/htmfilho/htmfilho.github.io.git
[uclouvain]: https://uclouvain.be
