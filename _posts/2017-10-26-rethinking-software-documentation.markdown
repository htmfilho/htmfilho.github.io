---
layout: post
title: "Rethinking Software Documentation"
date: 2017-10-21 12:00:00 +0200
categories: asciidoc
excerpt_separator: <!--more-->
---

Recently, I was reviewing a [pull request][pull-request] when I caught an
inconsistency between the code and the documentation. The image below shows a
new return case added to the function `is_program_manager`, but the developer
didn't not update the documentation accordingly. So, the text still explains the
previous return logic.

![Flagrant of outdated code documentation](/images/posts/code_documentation.png)

<!--more-->

Is it the developer's fault? Can (s)he be held accountable for this omission
even when the code runs as expected and passes all tests? I understood that the
names used to identify functions and variables were sufficiently clear to
understand the code. No documentation was actually needed. So, I didn't ask the
programmer to fix the documentation. It would mean an additional overhead to the
code reviewing process for something that doesn't cause compilation neither
runtime errors.

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

Earlier documentation doesn't have to be extensive. Done iteratively, it may
initially cover just enough content to enable a minimal viable product and then
progressively cover more and more features as the project advances. That's what
is stated in the agile manifesto.

> "Working software over comprehensive documentation."

This statement is often misunderstood. Recently talking to some consultants, I
realized they interpreted "comprehensive documentation" as a problem to be
solved with "no documentation at all". The disseminated approach is to be
limited by a post-its or index cards in an informal language description. Once
they are implemented they can be completely discarded, no strings attached. The
documentation is transient and summarized in a few sentences. If not registered
in an issue tracker, they are lost forever.

That's sad. Discarding real useful work disturbs me. Unless the users changed
their minds about the requirements or a major architectural flaw was discovered,
or something can be substantially improved, there is no reason to throw
something away. This is waste and waste is avoided in every industry. People's
work must be constructive, the results must be useful and valuable. But how can
this principle be applied on software documentation?

Actually, requirements have been often discarded since the waterfall age. It
wasn't discarded in the sense of throwing away, but in the sense of abandonment.

Nowadays, we rarely document software as before, and that's a good thing, but
we shouldn't be ignoring documentation all together. Let's see an example.

![assignment](/images/posts/form-volume-horaire.jpg)

![assignment-2](/images/posts/form-volume-horaire2.jpg)

![assignment-3](/images/posts/form-volume-horaire3.jpg)

All details about installing Asciidoctor on your system can be found on
[Asciidoctor's website][asciidoctor]. Here we consider the installation on
Ubuntu:

    $ sudo apt-get install asciidoctor

{% highlight python %}
import subprocess

def generate_pdf():
    subprocess.check_output(
           ['asciidoctor-pdf',
            '-a', 'pdf-stylesdir=resources/themes',
            '-a', 'pdf-styles=osis', "{}{}".format(path, "user-manual.adoc")])

def generate_html():
    subprocess.check_output(
           ['asciidoctor', "user-manual.adoc"])

def build():
    generate_pdf()
    generate_html()

if __name__ == '__main__':
    build()
{% endhighlight %}

A more feature-complete version of this code is available at the repository
[uclouvain/osis-internship][doc-build].

Execute it:

    $ python3 build.py

[asciidoctor]: http://asciidoctor.org/docs/install-toolchain/
[doc-build]: https://github.com/uclouvain/osis-internship/blob/master/docs/build.py
[documenting-complexity]: https://github.com/uclouvain/osis/blob/13f0ec5d7002aa8c33e922a121011ea51b066f59/internship/utils/student_assignment/solver.py#L89
[pull-request]: https://github.com/uclouvain/osis/pull/2656/files
