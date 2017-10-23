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

In my judgement, it isn't the developer's fault because the code was behaving as
expected and passing its tests. So, I didn't ask him to fix the documentation
because it means an additional overhead to the code reviewing process for
something that doesn't cause compilation neither runtime errors. In addition,
the names used to identify functions and variables were sufficiently clear to
understand the code. No documentation was actually needed.

On the othe hand, there are some cases where the business is difficult to
understand and the code needs to be well documented. As an example, we have
[an algorithm][documenting-complexity] that assigns students to internshipss
based on their individual constraints. The documentation is necessary because
the code is not trivial.

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
[uclouvain/osis-internship][doc-build]

Execute it:

    $ python3 build.py

[asciidoctor]: http://asciidoctor.org/docs/install-toolchain/
[doc-build]: https://github.com/uclouvain/osis-internship/blob/master/docs/build.py
[documenting-complexity]: https://github.com/uclouvain/osis/blob/13f0ec5d7002aa8c33e922a121011ea51b066f59/internship/utils/student_assignment/solver.py#L89
[pull-request]: https://github.com/uclouvain/osis/pull/2656/files
