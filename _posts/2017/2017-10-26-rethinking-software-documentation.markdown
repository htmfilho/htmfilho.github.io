---
layout: post
title: "Rethinking Software Documentation"
date: 2017-10-21 12:00:00 +0200
categories: asciidoc
excerpt_separator: <!--more-->
---

Recently, I was reviewing a [pull request][pull-request] when I caught an
inconsistency between a code snippet and its documentation. The image below shows a
new return case added to the function `is_program_manager`, but the developer
didn't update the documentation accordingly. So, the text still explains the
previous return logic.

![Flagrant of outdated code documentation](/images/posts/code_documentation.png)

<!--more-->

Is it the developer's fault? Can (s)he be held accountable for this omission
even when the code runs as expected and passes all tests? In the role of code
reviewer I understood that the names used to identify functions and variables
were sufficiently clear to make the code readable. No documentation was actually
needed. So, I didn't ask the programmer to fix the documentation. It would mean
an additional overhead to the code reviewing process for something that doesn't
cause compilation neither runtime errors.

On the other hand, there are some cases where it's difficult to represent the
business into code. As an example, we have [an algorithm][documenting-complexity]
that assigns students to internships based on their individual constraints. The
documentation is necessary because the code is not trivial.

Code documentation is sometimes useful, but it comes too late, when the code is
already written. There is another kind of documentation that comes first: the
specification. This term makes people scary these days because it is associated
with old fashion software processes, but it is just another name for use cases,
user stories, and other fancy synonyms created recently. The point is: The
documentation written earlier is a guidance to write code that effectively
serves the real intent, minimizing the frustration of developing something that
isn't useful for the users.

## Misunderstanding Agility

The agile manifesto states:

> "Working software over comprehensive documentation."

As every philosophical text, this manifesto is also subject of antagonic
interpretations. In my understanding, early documentation doesn't have to be
comprehensive. Done iteratively, it may initially have just enough content
to enable a minimal viable product and then progressively covering more and more
features as the project advances.

However, in recent talks to some consultants, I realized they interpreted
"comprehensive documentation" as a problem to be solved with "no documentation
at all". The disseminated approach is to be limited by post-its or index cards
in an informal language description. Once they are implemented they can be
completely discarded, no strings attached. The documentation is transient and
summarized in a few sentences. If not registered in an issue tracker, they are
lost forever.

That's sad. Discarding real useful work disturbs me. Unless the users changed
their minds about the requirements or a major architectural flaw was discovered,
or something can be substantially improved, there is no reason to throw
something away. This is waste and every industry avoids it. People's work must
be constructive, the results must be useful and valuable. But how can this
principle be applied on software development?

Actually, requirements have been often discarded since the waterfall age. It
wasn't discarded in the sense of throwing away, but in the sense of abandonment.
Architecture documents, use case specifications, project guidelines, deployment
models, they were created but seldom updated. It was very expensive to keep
documentation and implementation synchronized. Aparently, this problem hasn't
be solved yet by any agile methodology. There is indeed an opportunity of
rethinking - not reinventing - how documentation should be produced to achieve
durability and real added value.

## The User Manual

The problem with documentation in general is the lack of readers. With a boring
writing style and only developers as audience, a document will hardly be updated
as frequent as needed. As the software evolves, only verbal, visual (mock-ups,
diagrams, templates, etc.) and short textual communication (emails, issue
trackers) prevail. The rest remains forgotten into "dusty" folders.

We should rethink documentation to become something that people actually read,
enjoy, learn and share. Where errors and obsolescence are considered as serious
as bugs in software. It happens that documentation might be the primary reason
of software success. Classical examples are programming languages, frameworks
and platforms (software to build software) where the more documentation is
available the higher is the probability of adoption. Not so long ago, we decided
to adopt Django for business applications because of its extensive
documentation, which helps to reduce the learning curve. On the other hand, my
great passion for Clojure has been faded out because of too many gaps in its
documentation. Taking this for our businesses, a good documentation might be a
key success factor.

![Car owner manual](/images/posts/car-owner-manual.jpg)

**My answer to an effective documentation is to write it in the format of a user
manual**. As the sense of usability grows with good UI practices supported by
modern frameworks, the idea of writing a user manual seems to be absurd, until
the user asks for one. Take your car as an example. You are so used to drive
cars that when you took your current one for the first time, it just happened
naturally. You didn't even touch the owner's manual. But when the engine's red
indicator lights up, guess what comes first in your mind? Yes, that heavy manual.
You want to know the implications of continuing driving with that light on and
how much time you have before sending the car to maintenance.

You may say cars are different, old fashion stuff, that it isn't the same in
software. Well, not really. What your browser, your favorite text editor, Gmail,
Facebook and Google have in common ? They all have a help system, which is just
another name for user manual. You never noticed it until Facebook changed its
privacy rules or you wanted to [delete searches & other activity][google-help]
from your Google account. The fact that your users aren't doing the same in your
applications may explain why they aren't so happy using it.

![Gmail and Facebook help systems](/images/posts/help-gmail-facebook.png)

I have the audacity to say that the user manual is the most valuable
documentation, if not the only one, you can write for your application. These
are the main reasons why:

* The text is not disposable because it has too many readers, or potential
  readers, that will demand it to be updated.

* Writing a user oriented document will push you to think more about the user
  experience and develop better user interfaces.

* If written at the beginning as a way to elicit requirements, it will be also
  read by analysts, programmers, support analysts, project managers, product
  owners, and real users.

* Everybody around a single document, providing feedback, makes it continuously
  improved and updated.

* A user manual is the best guide to write [automated functional tests][selenium].
  When all tests pass then the user manual is also correct.

## Documentation as Code

[asciidoctor]: http://asciidoctor.org/docs/install-toolchain/
[Django]: https://www.djangoproject.com
[doc-build]: https://github.com/uclouvain/osis-internship/blob/master/docs/build.py
[documenting-complexity]: https://github.com/uclouvain/osis/blob/13f0ec5d7002aa8c33e922a121011ea51b066f59/internship/utils/student_assignment/solver.py#L89
[google-help]: https://support.google.com/websearch/answer/465?hl=en-BE&ref_topic=3378866
[Odoo]: https://www.odoo.com
[pull-request]: https://github.com/uclouvain/osis/pull/2656/files
[selenium]: http://www.seleniumhq.org
[Ubuntu]: https://www.ubuntu.com
