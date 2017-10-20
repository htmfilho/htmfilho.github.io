---
layout: post
title:  "Decomposing a Large Codebase Into Git Submodules"
date: 2017-10-19 12:00:00 +0200
categories: git
---

I recognize good developers by their capacity of cleaning existing code and
adding a minimal amount of code for new features. Their pull requests are
compact, favoring reusability and elegancy. But even with their effort, some
codebases are simply large because the implemented business are complex. This
is the case of OSIS, an open source software designed to manage the core
business of the Université catholique de Louvain.

OSIS is a monolithic Django project, composed of several applications. These
applications can have their own resources or share resources with other
applications. They can even be activated or deactivated in runtime, which means
the entire codebase is not necessarily running in production. This architecture
is so flexible that the IT department of the university decided to estimulate
other departments, in need of a business application, to develop apps for OSIS,
instead of other heterogenous choices. We kindly call them satellite apps in the
OSIS constellation. The strategy is working because three apps were already
developed in the last 18 months by three different teams.

However, those apps have tripled the OSIS' codebase, making it larger than what
was originally planned. It isn't so serious in the case of a Python project
because there is not such things like compilation, packaging or startup
time. But a large codebase is harder to maintain and, when developed by multiple
teams, may cause several workflow issues.

To address this problem, we picked one of the apps, externalized it in a
different repository and added it back to OSIS as a Git submodule. Some of you
may argue that `git subtree` would be a better option compared to `git
submodule` because of its transparency to other developers, but the commands are
so much more complex to configure, push and pull with the remote repository.
Actually, we have been working with `submodule` for a while and we had no major
issues so far. Others may also argue that its time for microservices. I don't
see it as an advantage just yet because we may reduce the codebase but we would,
at the same time, complexify the architecture with an additional web service
layer, additional secury measures and more configurations. We don't even have
the excuse of a performance issue, so the added value is obviously not there
yet.

## Moving the internship Folder to a New Repository

Here is a step by step guide of the commands I used to move the Internship app
to another repository and add it back as a submodule. Do avoid messing up with
my programming environment, I've decided to do everything in a temporary folder:

    $ cd ~/python/projects/osis
    $ mkdir temp

Then I cloned the OSIS repository inside of the temporary folder:

    $ cd temp
    $ git clone https://github.com/uclouvain/osis.git

To preserve the history of changes in the Internship app, I decided to start the
new repository from a clone of OSIS:

    $ git clone osis ./osis-internship
    $ cd osis-internship

In my case, the default branch of OSIS is `dev`. After cloning it, the branch of
`osis-internship` is also `dev`, so I have to create a `master` branch from
`dev`, but you don't have to do that if you cloned a `master` branch:

    $ git checkout -b master

At this point, the repository `osis-internship` is ready for the clean up. The
intention here is to remove all files that aren't part of Internship, put the
content of the folder `internship` in the root of the repository and remove the
folder `internship`:

    $ git rm -rf assessments/ backoffice/ assistant/ base/ dissertation/ \
                 reference/ attribution/ cms/ doc/ osis_common/ dev-settings.py \
                 Dockerfile __init__.py
    $ git mv internship/* .
    $ rm -rf internship

Let's commit these changes. In this project, we put the number of the issue we
are working on in the commit message:

    $ git commit -m "INTERNSHIP-1 Removed unecessary resources and moved the " \
                    "content of the folder 'internship' to the root."

The last steps for the repository `osis-internship` is to create a new
repository on GitHub, reset the remote origin to point to this new GitHub
repository and push the local master branch:

    $ git remote set-url origin https://github.com/uclouvain/osis-internship.git
    $ git push origin master

## Creating the Submodule in the OSIS Repository

Move back to osis, remove the folder `internship` and commit the change:

    $ cd ../osis
    $ git rm -rf internship/
    $ git commit -m "OSIS-195 Folder 'internship' removed."

Let's add the repository `uclouvain/osis-internship` as a submodule of `osis`:

    $ git submodule add https://github.com/uclouvain/osis-internship.git \
          ./internship
    $ git submodule init
    $ git submodule update

Finally, we commit and push the change to GitHub:

    $ git commit -m "OSIS-195 Submodule 'internship' added."
    $ git push origin dev

Voilà! The new submodule was added to the cobebase of OSIS, which is now
smaller, since a submodule is just a reference to another repository.

## How to Develop in the New Submodule

At this point, not even you are ready to develop the new submodule because we
did everything in a temporary folder. Let's get back to the working environment
and pull the latest changes:

    $ cd ~/python/projects/osis/osis
    $ git pull origin dev

Then, let's set up the local submodule:

    $ git submodule init
    $ git submodule update

We are all set to start. After this initial set up the only command you need to
remember is:

    $ git submodule update

which will be useful when somebody else updates the reference to the `internship`
repository but you don't have the lastest modifications in your local
machine yet.

We have a repository inside of another one. So, when we are at the `osis`
repository and type `git status` we see the active branch is `dev`. But when we
enter in the submodule `internship` and type `git status`, we see the active
branch is `master`. These repositories have different remote origins
