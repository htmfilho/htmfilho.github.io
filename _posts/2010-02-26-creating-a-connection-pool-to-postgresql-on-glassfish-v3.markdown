---
layout: post
title: "Creating a Connection Pool to PostgreSQL on Glassfish V3"
date: 2010-02-26 09:32:00 +0200
categories: uncategorized database enterprise application open source
---

I recently created a new connection pool to PostgreSQL on Glassfish and I would like to share the steps I followed with you. Obviously, you need <a href="http://www.postgresql.org/">PostgreSQL</a> and <a href="http://glassfish.dev.java.net/">Glassfish</a> installed on your machine and a database already created in PostgreSQL. If you didn’t configure your new PostgreSQL installation yet, follow the steps I described at this <a href="http://69.89.31.239/~hildeber/?p=190">previous post</a> and come back here to continue with the connection pool. The necessary steps are:

<ol>
<li>We need the PostgreSQL JDBC Driver, since Glassfish and its deployed applications are writen in Java. Drivers are available for download at <a href="http://jdbc.postgresql.org/" target="_blank">http://jdbc.postgresql.org</a>. For this experiment choose the JDBC4 driver.</li>
<li>Download the driver file <i>postgresql-<version>.jdbc4.jar</i> and copy it to the diretory <i>[glassfish_home]/glassfish/domains/domain1/lib/</i>.</li>
<li>Restart Glassfish in order to make it load the new database driver. I thought that adopting an OSGI architecture Glassfish would never need restarts again, but I was wrong. At least, the restarting process is faster than V2.</li>
<li>Enter in the administration console and go to <i>Resources/JDBC/Connection Pools</i>.</li>
<li>Create a new connection pool with the name <i>[database_name]Pool</i>, select the resource type <i>javax.sql.ConnectionPoolDataSource</i>, select the database vendor <i>PostgreSQL</i> and click next.</li>
<li>Select the datasource classname <i>org.postgresql.ds.PGConnectionPoolDataSource</i> and inform the following additional properties:<br/><i>DatabaseName=[database-name]</i><br/><i>Password=*******</i> 😉<br/><i>PortNumber=5432</i> (this is the default port but make sure that you are using the correct one)<br/><i>ServerName=[server-name|ip]</i><br/><i>User=<database-username></i></li>
<li>Click <i>Finish</i> to save the new connection pool.</li>
<li>Go to the list of connection pools again and select the new one that you just created.</li>
<li>Click on <i>Ping</i> to check if the connection was correctly configured. The message “Ping Succeeded” means that the connection is working fine.</li>
<li>In order to be able to use this connection pool in JEE applications, we have to create a JNDI name for it. Go to <i>Resources/JDBC/JDBC Resources</i>.</li>
<li>Click on <i>New</i> and set the JNDI Name <i>jdbc/[database_name]</i>, select the connection pool created above and click <i>Ok</i> to finish. This JNDI name will be used by applications to access the PostgreSQL database.</li>
</ol>
These instructions may work with Glassfish V2 as well, since its database configuration is quite similar.

I’m being very specific in terms of chosen technologies, but if you have a slightly different configuration and these steps are not working yet, please comment your issues below, describing also your current configuration/context. Maybe, we can figure it out.
