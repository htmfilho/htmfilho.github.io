---
layout: post
title: "Before Starting to work with PostgreSQL"
date: 2007-09-10 09:05:00 +0200
categories: database
---

Who starts to work with PostgreSQL on Linux has a bad initial experience: to do the first authentication.  The installation process of this database server creates a SO user, the `postgres`, which has super user access, able to do all initial steps of a beginner programmer, like to create users and databases. But, how can we use this user if we don’t know its password?<br/>I followed the steps below, which was compiled from different Google’s sources:

1. change to the root user or a sudo user, who is able to change to another user without informing its password:<br/>`# su root`<br/>or jump step 2 doing:<br/>`# sudo su postgres`

2. change to the Postgres user:<br/>`# su postgres`

3. create a database server user with the same username of yours:<br/>`# createuser -d -r -s -P (your_user_name)`<br/>This command will create a database server super user, able to create  new databases and roles. The command will request a password and then  the user will be created.

4. change to your user:<br/>`# su (your_user_name)`

5. execute the command to create a database:<br/>`# createdb (database-name)`
