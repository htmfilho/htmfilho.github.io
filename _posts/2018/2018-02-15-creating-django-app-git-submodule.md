---
layout: post
title:  "Creating a Django App as a Git Submodule"
date: 2018-02-15 12:00:00 +0200
categories: git submodule python django osis
---

![Lego bricks](/images/posts/creating-git-submodules.jpg)

In a [recent post][previous-post], I explained how to decompose a large codebase into [Git submodules][git-submodule]. In that occasion, I explained how we did that in the [OSIS] project for existing applications. This time, I'm going to explain the creation of a new submodule that isn't a relocation of an existing application, but a brand new application for new users.

<!-- more -->

It is going to be easier this time. We practically start from the middle of the previous post. The first step is to create a new repository on [GitHub] for the new app. Please, follow the instructions there. The only suggestion I give is to follow a naming convention. In the case of OSIS, we prefix the submodules with the name of the project, followed by a dash and then the name of the app. For example:

    osis-mobility

This way, the repositories are semantically grouped:

    osis
    osis-common
    osis-internship
    osis-mobility

## Creating the Submodule in the Main Repository

I go to the local clone of the repository to integrate the new submodule:

    $ cd ~/python/projects/osis
    $ git submodule add https://github.com/uclouvain/osis-mobility.git ./mobility
    $ git submodule init
    $ git submodule update

Notice that I'm not allowing Git to create the directory with the default name `osis-mobility`. I'm passing by parameter the name I want it to be: `./mobility`. I removed the prefix `osis-` from the name to avoid ambiguity with the main repository, which is named `osis`.

To finish, commit the new submodule:

    $ git add mobility
    $ git commit -m "submodule 'mobility' added to the project."

From the Git perspective it is done. So, if you are programming in a language different from Python and a framework different from [Django], then you know what to do afterwards.

## The Submodule as a Django App

From this point on, I focus on a Django app. I'm using django-admin to create that app in the new repository:

    $ source venv/bin/activate
    $ cd mobility
    $ django-admin startapp mobility .

To be able to run the command `django-admin` I had to activate the virtual environment of the project. The `.` after `mobility` is very important because it generates the files in the current directory instead of creating a new directory.

To integrate the new app, I add it to the list of `INSTALLED_APPS` in the `settings.py` file:

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'whitenoise.runserver_nostatic',
        'django.contrib.staticfiles',
        ...
        'mobility',
    ]

Then I just have to commit the new files and push your changes.

    $ git add .
    $ git commit -m "Initial commit"
    $ git push origin master

Finally, I update the reference of the submodule to the latest commit:

    $ cd ..
    $ git add mobility
    $ git commit -m "Updated the reference of the mobility app"

Voilà! The new app was added to the project. It's ready to be further developed in an independent lifecycle. The [previous post][previous-post] gives more details about what to do from this point on.

[Django]: https://www.djangoproject.org
[Github]: https://www.github.com
[git-submodule]: https://git-scm.com/docs/git-submodule
[OSIS]: https://github.com/uclouvain/osis
[previous-post]: http://www.hildeberto.com/2017/10/decomposing-into-git-submodules.html
[Python]: https://www.python.org
