---
layout: post
title: "Converting CSV to SQL with GoGetSQL"
date: 2021-05-25 12:00:00 +0200
categories: golang csv sql library
---

![Gopher processing data](/images/posts/converting-csv-sql.jpg)

CSV is the defacto Most of database management systems support Using a cloud provider to run our business has been a game changer. Azure allow us to rapidly provision all the resources to ensure high availability, security, and performance. In many cases, Azure provides and also manages resources for us, considerably reducing complexity and saving time. However, the more control we delegate to Azure the less autonomy we have over those resources. This is a good thing because it pushes towards the adoption of good practices, but it can be challenging sometimes.

<!-- more -->

Take the provision of a managed SQL Server, for example. Azure ensures it is optimally configured for our needs, but it is quite limited when it comes to seeding the database using a CSV file. The procedure can only be done on Windows, for example. When it comes to other databases, such as PostgreSQL or MySQL, it cannot be done at all.

![Waterloo Street Trees](/images/posts/waterloo-street-trees.png)

To solve this problem to all platforms and all SQL databases on Azure, we have developed a simple tool capable of converting a CSV file into a SQL file, where entries turn into insert statements. It is called GoGetSQL. All you need after using GoGetSQL is a mean to execute the final script, which is something we are pretty well served. As an example, consider the following dataset:

Whose representation in CSV is the following:


GoGetSQL converts it into SQL using the following command on Windows:

    $ csvtosql.exe —-csv=path\to\mapping.csv

Or on MacOS:

    $ ./csvtosql —-csv=path/to/mapping.csv

Here is a sample of the result:


This is what happens by default: 

- the name of the CSV file is used as the name of the table in the insert statement
- the first line is skipped because it labels the data 
- the labels in the first line are used as columns of the table
- the column separator is comma
- each line in the CSV turns into an insert statement
- all values were considered as string, even the numeric target_code.

These default behaviours can be change if needed. To set the table name different from the file name, use: 

    —-table=standard_mapping

If the first line contains data instead of labels then it can also be considered using:

    —-includefirstline

If the labels in the first line don’t match the column names in the table then we can customize them this way:

    -—columns='source_code(text),source_system(text),code(number),system(text),definition(text)'

Notice that it also allows defining the types of the columns, resulting in the following SQL statement:

    insert into standard_mapping (source_code, source_system, code, system, definition) values ('M71.17','ICD10CM',122482001,'SNOMED','Infected bursa');

The table and the columns’ names have changed accordingly and the code column is now numeric.

Last, but not least, the CSV used comma as separator, but it could be using tabs as well. For a CSV like this: 

```
K40.4 ICD10CM 2303007 SNOMED Inguinal hernia with gangrene
S34.3XXD ICD10CM 230614002 SNOMED Injury of caudal equina
```

we would add the flag:

    —-separator=tab

Sometimes the CSV file is too large and generates too many insert statements to the point a single database transaction cannot cope. To create several transactions use the flag:

    —-chunk=1000

It puts thunks of 1000 inserts between begin transaction and commit transaction. The insert statements can be further optimized, inserting several records at once by using the flag:

    —-chunkinsert=250

It generates insert statements in this format:


A proper configuration of --chunk and --chunkinsert can optimize the SQL file for maximum performance. In this case, a CSV file with 10000 records would be converted into a SQL with 10 transaction thunks and each transaction would contain 4 insert statements with 250 records each.

Last, but not least, we have --prefix and --suffix to put content at the beginning and at the end of the sql file:

    --prefix=path/to/prefix.sql
    --suffix=path/to/suffix.sql

The prefix.sql and the suffix.sql files are actually templates and support the table name. For example:

```
create table {{ .Table }} (
    source_code        varchar(50)  not null,
    source_description varchar(300) not null,
    source_system      varchar(100) not null,
    source_version     varchar(300) not null,
    target_code        varchar(50)  not null,
    target_description varchar(300) not null,
    target_system      varchar(100) not null,
    target_version     varchar(300) not null
);
```

`{{ .Table }}` can also be used multiple times in the file:

```
create index {{ .Table }}_idx on {{ .Table }} (source_code, source_system, target_system);
```

Installation
GoGetSQL is a command line tool developed by engineers for engineers, but as you can see it is pretty easy to use by anyone. If you are convinced that GoGetSQL can improve your productivity then let’s move on to the installation.

GoGetSQL binaries are not promptly available. It can only be installed from source. The installation starts by enabling your workstation to fetch the source code and build it. For that, you need Git and the Go compiler:

Install Go by following the instructions for your operating system:
https://golang.org/doc/install

Install Git by following the instructions for your operating system:
https://git-scm.com/downloads

## On Windows

On the Windows Command Prompt, fetch the source code in your workstation:

```
\> cd c:\dev\software
\> git clone https://git.pointclickcare.com/scm/~mendoh/gogetsql.git
```

and compile it:

```
\> cd gogetsql
\> go build csvtosql.go
```

The build generates the file csvtosql.exe, which is all you need to convert your CSV files into SQL.

## On MacOS

Fetch the source code in your workstation:

```
$ cd ~/dev/software
$ git clone https://git.pointclickcare.com/scm/~mendoh/gogetsql.git
```

Compile it:

```
$ cd gogetsql
$ go build csvtosql.go
```

The build generates the file csvtosql, which is all you need to convert your CSV files into SQL.

Binaries can also be built targeting different operating systems:

```
$ GOOS=darwin GOARCH=amd64 go build csvtosql.go
$ GOOS=windows GOARCH=amd64 go build csvtosql.go
```

GoGetSQL is very new and serves our projects very well, but there is always a chance GoGetSQL is not generic enough to cover your needs. I would love to make it work for you too, so comment below if you are facing a problem or write me an email directly with your questions or needs.