---
layout: post
title:  "Table Versioning With Liquibase"
date: 2020-12-21 12:00:00 +0200
categories: database java
---

![Programming Activity](/images/posts/table-versioning-liquibase.png)

Imagine you have an application that needs to be extremelly precise about the address of the people it manages. It has low tolerance for mistakes like typos, mispelings, and even imaginary locations. To ensure precision, you have a complete list of all countries, states, provinces, cities and postal codes to assist users on filling-in correct addresses.That's a lot of data from an external data provider that periodically releases new versions of the dataset. The question is: how to update the data without any downtime?

<!-- more -->

This is an application scenario where some tables of the database have a considerable volume of data that come from external sources and would be hard to update without a sofisticated logic to calculate the delta. There are many solutions for this problem. The one we are going to discuss now is the creation and load of a new version of the table that will contain the updated data. While the process is running the application is serving data from the current version and automatically switches to the new table when the process finishes.

To implement this tactic, we need the help of a database migration tool such as [Liquibase]. It is capable of running database scripts during the deployment of the application. It helps to keep application and database changes tied together so the database can be improved without breaking the application. That's what we need to create the table, load the data, create indexes and clean up old data.

Liquibase generates the table `DATABASECHANGELOG` to keep track of migrations the first time it runs. In this table, we are interested in the column `ORDEREXECUTED` that contains the sequence in which the migrations files were executed. We use this sequence to reference the versions of the tables. The first execution would generate and populate tables like:

    country_v1
    state_v1
    city_v1
    postal_code_v1

The number 1 is the maximum value in the column `ORDEREXECUTED`. The second execution would generate and populate another version:

    country_v2
    state_v2
    city_v2
    postal_code_v2

The application needs to implement a logic to swift from `v1` to `v2` when the process of creating `v2` is finished. This query gets the most recent order:

{% highlight sql %}
select max(orderexecuted) as version
from databasechangelog
where EXECTYPE = 'EXECUTED';
{% endhighlight %}

Taking the result of this query and concatenating it with the table name we get the newest version of the table:

    table = "country_v" + version  // Ex.: country_v8

With this new table name we can then query it:

    query = "select name, acronym from " + table + " where ..."

The migration file must be composed of 4 parts:

   1. creating the new version of the tables without indexes to improve insert operations

   2. seeding the tables with updated records

   3. creating the indexes

   4. removing tables created two versions ago

For example:

{% highlight sql %}
--liquibase formatted sql

--changeset versioner:3

-- 1. creating the new version of the table
create table country_v3 (
    acronym varchar(3)  not null,
    name    varchar(50) not null
);

-- 2. seeding the tables with updated records
insert into country_v3 (acronym, name) values
    ('AUS', 'Australia'),
    ('BRA', 'Brazil'),
    ('CAN', 'Canada'),
    ...
    ('URU', 'Uruguay');

-- 3. creating the indexes
create unique index idx_country_v3_acronym on country_v3 (acronym);

-- 4. removing tables created two versions ago
drop table country_v1;
{% endhighlight %}

Depending on the volume of data to be seeded, it might be interesting to wrap chunks of inserts into a transaction scope. We can wrap chunks of 10 thousands records with `begin transaction` and `commit transaction` to use less database resources.

This approach has a limitation. It only works if the migration files are exclusively used to version the tables. If intermediary migrations are executed then it will require extra attention to the column `ORDEREXECUTED` since the versioning sequence will experience some hiccups. This extra attention is a major cause of human error. To solve this limitation we can create an extra table to manage the versions:

{% highlight sql %}
create table versioning (
    version      integer  not null,
    version_date datetime not null default current_timestamp
);
{% endhighlight %}

In this case migration scripts would have a fifth step:

{% highlight sql %}
-- 5. increment the version
insert into versioning (version) values (3);
{% endhighlight %}

And the query to get the version changes too:

{% highlight sql %}
select max(version) as version
from versioning;
{% endhighlight %}

A third option, simpler than the `versioning` table, would be a configuration entry or an environment variable set with the version number. A configuration entry would take effect right after the deployment, which is required when working with multiple instances.Changing an environment variable may not be in sync with the app deployment, which may require more careful deployment procedures. 

To prevent downtime the application would need at least 2 live instances. While the first one is upgrading, therefore creating and seeding the new version of the table, the other ones are still serving data from the current version. The first one is the first to serve data from the new version and the next ones will follow as they get upgraded too.

Another possibility is to use Liquibase for table versioning and [Flyway] for other migration needs, but I didn't have time to test this posibility yet. Did you?

[Flyway]: https://flywaydb.org
[Liquibase]: https://www.liquibase.org