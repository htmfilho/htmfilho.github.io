---
layout: post
title:  "The Software Documentation Dilema"
date: 2017-07-12 19:32:05 +0200
categories: documentation
---

Recently, I was reviewing a
[pull request](https://github.com/uclouvain/osis/pull/2656/files) when I caught
an inconsistency between the code and the documentation. The image below shows
a new return case added to the function `is_program_manager`, but the developer
didn't not update the documentation accordingly. So, the text still explains the
previous return logic.

![Flagrant of outdated code documentation](/images/posts/code_documentation.png)

In my judgement, it isn't the developer's fault because the code was behaving as
expected and passing its tests. So, I didn't ask him to fix the documentation
because it means an additional overhead to the code reviewing process for
something that doesn't cause compilation neither runtime errors.
