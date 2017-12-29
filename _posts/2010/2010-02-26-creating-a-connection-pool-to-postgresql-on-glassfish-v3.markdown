---
layout: post
title: "Creating a Connection Pool to PostgreSQL on Glassfish V3"
date: 2010-02-26 09:32:00 +0200
categories: database enterprise application open source
---

I recently created a new connection pool to PostgreSQL on Glassfish and I would like to share the steps I followed with you. Obviously, you need <a href="http://www.postgresql.org/">PostgreSQL</a> and <a href="http://glassfish.dev.java.net/">Glassfish</a> installed on your machine and a database already created in PostgreSQL. If you didn’t configure your new PostgreSQL installation yet, follow the steps I described at this <a href="http://69.89.31.239/~hildeber/?p=190">previous post</a> and come back here to continue with the connection pool. The necessary steps are:

1. We need the PostgreSQL JDBC Driver, since Glassfish and its deployed applications are writen in Java. Drivers are available for download at <a href="http://jdbc.postgresql.org/" target="_blank">http://jdbc.postgresql.org</a>. For this experiment choose the JDBC4 driver.

1. Download the driver file `postgresql-<version>.jdbc4.jar` and copy it to the diretory `[glassfish_home]/glassfish/domains/domain1/lib/`.

1. Restart Glassfish in order to make it load the new database driver. I thought that adopting an OSGI architecture Glassfish would never need restarts again, but I was wrong. At least, the restarting process is faster than V2.

1. Enter in the administration console and go to `Resources/JDBC/Connection Pools`.

1. Create a new connection pool with the name `[database_name]Pool`, select the resource type `javax.sql.ConnectionPoolDataSource`, select the database vendor `PostgreSQL` and click next.

1. Select the datasource classname `org.postgresql.ds.PGConnectionPoolDataSource` and inform the following additional properties:<br/>`DatabaseName=[database-name]`<br/>`Password=*******`<br/>`PortNumber=5432` (this is the default port but make sure that you are using the correct one)<br/>`ServerName=[server-name|ip]`<br/>`User=<database-username>`.

1. Click "Finish" to save the new connection pool.

1. Go to the list of connection pools again and select the new one that you just created.

1. Click on "Ping" to check if the connection was correctly configured. The message "Ping Succeeded" means that the connection is working fine.

In order to be able to use this connection pool in JEE applications, we have to create a JNDI name for it:

1. Go to `Resources/JDBC/JDBC Resources`.

1. Click on "New" and set the JNDI Name `jdbc/[database_name]`, select the connection pool created above and click "Ok" to finish. This JNDI name will be used by applications to access the PostgreSQL database.

These instructions may work with Glassfish V2 as well, since its database configuration is quite similar.

I’m being very specific in terms of chosen technologies, but if you have a slightly different configuration and these steps are not working yet, please comment your issues below, describing also your current configuration/context. Maybe, we can figure it out.
