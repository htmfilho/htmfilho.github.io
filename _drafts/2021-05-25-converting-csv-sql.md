---
layout: post
title: "Converting CSV to SQL with GoGetSQL"
date: 2021-05-25 12:00:00 +0200
categories: golang csv sql library
---

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
