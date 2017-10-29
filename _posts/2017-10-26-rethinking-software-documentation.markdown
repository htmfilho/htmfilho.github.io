---
layout: post
title: "Rethinking Software Documentation"
date: 2017-10-21 12:00:00 +0200
categories: asciidoc
---

Recently, I was reviewing a [pull request][pull-request] when I caught an
inconsistency between the code and the documentation. The image below shows a
new return case added to the function `is_program_manager`, but the developer
didn't not update the documentation accordingly. So, the text still explains the
previous return logic.

![Flagrant of outdated code documentation](/images/posts/code_documentation.png)

<!-- more -->

In my judgment, it isn't the developer's fault because the code was behaving as
expected and passing its tests. So, I didn't ask him to fix the documentation
because it means an additional overhead to the code reviewing process for
something that doesn't cause compilation neither runtime errors. In addition,
the names used to identify functions and variables were sufficiently clear to
understand the code. No documentation was actually needed.

On the other hand, there are some cases where the business is difficult to
understand and the code needs to be well documented. As an example, we have
[an algorithm][documenting-complexity] that assigns students to internships
based on their individual constraints. The documentation is necessary because
the code is not trivial.

## Misunderstanding Agility

Leaving the code aside, there is another kind of documentation that is in frank
decay, mainly because of the agile manifesto stating:

> "Working software over comprehensive documentation."

This is a totally valid statement, but people interprets the part of
"comprehensive documentation" as "no documentation at all". Comprehensive
documentation is something I learned in early 2000s because of the great success
of RUP (Rational Unified Process) and CMM (Capability Maturity Model). At that
time, Agile and REST were disruptive practices that ended up dominating the
market years later. But we had no choice but to produce tons of documents
describing something that was changing all the time: software.

Nowadays, we rarely document software as before, and that's a good thing. The
problem with that kind of documentation is the lack of readers. If a document
targets only reviewers and developers it is hardly updated. As the software
evolves, only verbal, visual (mock-ups, some diagrams, templates, etc.) and
short textual (emails, issue trackers) communication prevails. The rest remains
forgotten into "dusty" folders, sometimes used as a notepad to draw more useful
artifacts. But we shouldn't be ignoring documentation all together.

We should think about a kind of documentation that people actually read, enjoy,
learn and share. Where errors and obsolescence are considered as bugs to be
urgently fixed, with the same pressure as bugs in software. In some cases,
poor documentation might be the primary reason of a software failure. Classical
examples are programming languages, frameworks and platforms (software to build
software) where the more documentation is available the higher is the
probability of adoption. Citing a personal example, I recently recommended the
rejection of an ERP system called [Odoo] simply because of its lack of updated
documentation for plugin developers. We would need a consultant all the time to
address all our questions, which is not practical neither cheap. We ended up
using [Django] because of its extensive documentation, which was interpreted as
a low risk adoption.

![Car owner manual](/images/posts/car-owner-manual.jpg)

## The User Manual

My answer to an effective documentation is to write it in the format of a **user
manual**. As the sense of usability grows with good UI practices supported by
modern frameworks, the idea of writing a user manual seems to be absurd, until
the user asks for one or simply abandon the app because it doesn't have one.
Take your car as an example. You are so used to drive a car that when you took
the current one for the first time, it just happened naturally. You didn't even
touch the owner's manual. But when the engine's red indicator lights up, guess
what comes first in your mind? Yes, the manual. You want to know the
implications of continuing driving with that light on and how much time you have
before sending the car to maintenance.

You may say cars are different, old fashion stuff, that it isn't the same in
software. Well, not really. What your browser, your favorite text editor, Gmail,
Facebook and Google have in common ? They all have a help system, which is just
another name for user manual. You never noticed it until Facebook changed its
privacy rules or you wanted to [delete searches & other activity][google-help]
from your Google account. The fact that you are not doing the same in your
application may explain why your users are not so happy using it.

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

All details about installing Asciidoctor on your system can be found on
[Asciidoctor's website][asciidoctor]. For practical reasons, we consider here
the installation on [Ubuntu] only:

    $ sudo apt-get install asciidoctor asciidoctor-pdf

{% highlight python %}
import subprocess

def generate_html():
    subprocess.check_output(
           ['asciidoctor', "user-manual.adoc"])

def generate_pdf():
    subprocess.check_output(
           ['asciidoctor-pdf',
            '-a', 'pdf-stylesdir=resources/themes',
            '-a', 'pdf-styles=osis', "{}{}".format(path, "user-manual.adoc")])

def build():
    generate_html()
    generate_pdf()

if __name__ == '__main__':
    build()
{% endhighlight %}

A more feature-complete version of this code is available at the repository
[uclouvain/osis-internship][doc-build].

Execute it:

    $ python3 build.py

[asciidoctor]: http://asciidoctor.org/docs/install-toolchain/
[Django]: https://www.djangoproject.com
[doc-build]: https://github.com/uclouvain/osis-internship/blob/master/docs/build.py
[documenting-complexity]: https://github.com/uclouvain/osis/blob/13f0ec5d7002aa8c33e922a121011ea51b066f59/internship/utils/student_assignment/solver.py#L89
[google-help]: https://support.google.com/websearch/answer/465?hl=en-BE&ref_topic=3378866
[Odoo]: https://www.odoo.com
[pull-request]: https://github.com/uclouvain/osis/pull/2656/files
[selenium]: http://www.seleniumhq.org
[Ubuntu]: https://www.ubuntu.com
