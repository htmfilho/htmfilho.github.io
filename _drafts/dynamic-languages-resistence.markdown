---
layout: post
title:  "The Dynamic Languages Resistence"
date: 2017-07-12 19:32:05 +0200
categories: documentation
---

The code below is a class that inherits from a Django ORM class that represents
a table in the database.

{% highlight python %}
class SessionExam(models.Model):
    external_id = models.CharField(max_length=100, blank=True, null=True)
    changed = models.DateTimeField(null=True, auto_now=True)
    number_session = models.IntegerField(choices=number_session.NUMBERS_SESSION)
    learning_unit_year = models.ForeignKey('LearningUnitYear')
    offer_year = models.ForeignKey('OfferYear', blank=True, null=True)
    progress = None
{% endhighlight %}

You don't have to understand what it is and its mechanics. The only thing I want
you to understand is that the field `offer_year` is not useful anymore in this
project. It is deprecated and to avoid any future confusion, it must be removed
soon so people don't use it. But before removing it, I have to check if it is
still used somewhere in the code, so I can fix those useless references.

To solve this problem in a statically typed language I would simply remove the
field and compile the code. If the field is still in use, then the compilation
would break, showing all the lines that have to be fixed before going through
the compilation phase. If you have a few thousands lines to check, then no
problem, but you would suffer in a large scale software.


Go is a fast, statically typed, compiled language that feels like a dynamically typed, interpreted language.
