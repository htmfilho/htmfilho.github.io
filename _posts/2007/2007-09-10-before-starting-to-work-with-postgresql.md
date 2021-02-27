---
layout: post
title: "Before Starting To Work With PostgreSQL"
date: 2007-09-10 09:05:00 +0200
categories: database postgres
---

![Before starting to work with PostgreSQL](/images/posts/2007-09-10-before-starting-to-work-with-postgresql.png)

Who starts to work with PostgreSQL on Linux has a bad initial experience doing the first authentication. The installation process of this database server creates a `SO` user, the `postgres`, which has super user access, able to do all initial steps of a beginner programmer, like to create users and databases. But, how can we use this user if we don’t know its password?

<!-- more -->

I followed the steps below, which was compiled from different Google’s sources:

1. change to the root user or a sudo user, who is able to change to another user without informing its password:

   `# su root`
   
   or jump step 2 doing:
   
   `# sudo su postgres`

2. change to the Postgres user:

   `# su postgres`

3. create a database server user with the same username of yours:

   `# createuser -d -r -s -P (your_user_name)`
   
   This command will create a database server super user, able to create new databases and roles. The command will request a password and then the user will be created.

4. change to your user:

   `# su (your_user_name)`

5. execute the command to create a database:

   `# createdb (database-name)`
