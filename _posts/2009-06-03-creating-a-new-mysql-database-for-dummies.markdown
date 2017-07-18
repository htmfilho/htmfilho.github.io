---
layout: post
title: "Creating a New MySQL Database for Dummies"
date: 2009-06-03 09:50:00 +0200
categories: database
---

I’m writing this post for self reference because I always forget how I’ve created my last MySQL database. Well, I’m sharing because it could be useful for you too. I consider that you already have MySQL 5.0 or superior installed and running normally. I also consider that you configured the path of your operating system, pointing to the bin folder where all MySQL commands are located. If you don’t fulfill this prerequisites, you can easily find solutions for each one using Google. It depends on your operating systems, so I would never be complete here.

I’m going to use the basics, avoiding specific tools that can accelerate the process, because if you fulfill the prerequisites then I know you have these basics. So, execute the command below to start:

    $ mysql -u root -p

It will create a client authenticated session to access MySQL. “-u” means that you are passing the user of the session in the command line and “-p” means that you want to type the password right after the command has been executed. The user “root” has enough rights to create the database, but we will not use it all the time. Once authenticated, type the command below to create the database and a dedicated user for it:

    mysql> create database book_shop;
    mysql> create user 'bs_user'@'localhost' identified by ’(password)’;
    mysql> use book_shop;
    mysql> grant all privileges on book_shop.*
           to 'bs_user'@'localhost';
    mysql> flush privileges;

The database will be created, a new user too and finally we give all privileges for this user to operate the new database. To check if the database was appropriately created, execute the following command:

    mysql> show databases;

Check if the database “book_shop” is in the list. It should be ;). Then we have to sign out from this root’s session and open a new session for the new user to create the database structure. Please, follow the sequence of commands below:

    mysql> quit;
    $ mysql -u bs_user -p
    mysql> use book_shop;
    mysql> source (path of the database script)/script.sql;

Well, that’s it! You should use the new user, `bs_user`, in your application avoiding the super powerful root guy. My intention is not to be complete on this post, but helpful. Maybe you can find a lot of additional good practices out there but this is the fastest technique I recommend you to do in order to start developing your project.

Any question? You know… comment below 😉 !
