---
layout: post
title: "First Release of Roma"
date: 2022-02-08 12:00:00 +0200
categories: portfolio repository rust csv sql
---

![Waterloo Tree Inventory](https://www.hildeberto.com/roma/images/waterloo_tree_inventory.png)

The [City of Waterloo](https://waterloo.ca), located in Ontario - Canada, has an [Open Data Portal](https://data.waterloo.ca) that publishes raw data about infrastructure, services, environment, transportation, etc. Residents can use the data to oversee public investments and services, identify gaps, discover development opportunities, and even create new business. We figured out another use for the Portal: **test [Roma](https://github.com/htmfilho/roma)**. It publishes a variety of CSV files. Among them, we found a an [inventory of every single tree planted on the streets](https://data.waterloo.ca/datasets/street-tree-inventory) of Waterloo. Isn't it cool?!

<!-- more -->

Roma is one of the repositories in my portfolio. I first introduced it [a month ago](https://www.hildeberto.com/2021/12/repositories-portfolio.html). Its goal is to convert a CSV file to a SQL file with insert statements, simplifying the data ingestion in relational databases. To have fun building Roma, we looked for an interesting dataset in the Open Data Portal and put it in the folder [/examples](https://github.com/htmfilho/roma/tree/main/examples). We are glad to inform that we've got the minimal Rust code in place to convert those CSV files to SQL. Roma implements convention over configuration, with the following default behaviors:

- the name of the CSV file is used as the name of the table in the insert statements.

- the first line is skipped because it contains the headers that describe the columns.

- the headers in the first line are used as columns of the table.

- the column separator is comma.

- each line in the CSV turns into an insert statement.

- if the value contains at least one alphanumeric character then it is quoted, but if the value contains a valid number then it is not quoted.

If you have these basic requirements then Roma is ready for you. Otherwise, wait for the availability of arguments that will customize these conventions. For the moment, simply type:

    $ roma --csv waterloo_tree_inventory.csv

It converts this CSV:

    X,Y,OBJECTID,TREEID,CIVIC_NO,STREET,LOCATION,SPECIES_NAME,SPECIES_LATIN,SPECIES_CODE,LANDUSE,ROADSEGMENTID,PARK,WARD,PLANTED_BY,MONTH_PLANTED,YEAR_PLANTED,STOCK_TYPE,STOCK_SIZE,STATUS,STATUS_DATE,CREATE_BY,CREATE_DATE,CREATE_YEAR,CREATE_MONTH,UPDATE_BY,UPDATE_DATE,SOURCE,SOURCE_DATE,OWNERSHIP,CATEGORY,ROOT_PATHWAYS,SOIL_VOLUME_M3,INITIAL_ACCEPTANCE_DATE,FINAL_ACCEPTANCE_DATE,OVERHEAD_HYDRO,DEVELOPMENT_AGE,PLANNING_COMMUNITY,SUB_WATERSHED,MAP_DBH_CM,GIS_NOTES,HEIGHT_ESTM_LIDAR_2014_M,HEIGHT_ESTM_LIDAR_2019_M,TAG1,GLOBALID,INSPECTED_YEAR
    -80.5095189090518,43.412175164406,1,10007057,27,ACTIVA AVE,BOULEVARD,Autumn Brilliance Serviceberry,Amelanchier x grandiflora 'Autumn Brilliance',AMGRAB,ROW,40056,,5,CITY CONTRACTOR,NOVEMBER,2014,BALL AND BURLAP,50 mm,REMOVED,2020/07/30 12:53:44+00,,2015/12/23 10:34:03+00,2015,December,GIS_DATA,2018/03/05 17:14:35+00,Tree Inventory,,CITY,Small Tree,N,,,,None,1997,LAURENTIAN WEST,BORDEN CREEK,7,ADAM BUITENDYK,0,10,,0a2719cc-94b2-42c7-80b7-5dc0c5fe0f24,
    -80.4806046253164,43.4464481686235,2,153401,10,CAMERON ST N,LAWN,Norway Maple,Acer platanoides,ACPL,ROW,11547,,10,UNKNOWN,UNKNOWN,0,UNKNOWN,UNKNOWN,ACTIVE,2017/01/31 15:14:06+00,Mark Grondin,2009/10/17 00:00:00+00,2009,October,Esri_Anonymous,2017/01/31 20:14:06+00,Tree Inventory,2009/10/17 00:00:00+00,CITY,Maple_Norway,N,,,,Three phase,1908,KING EAST,UPPER SCHNEIDER CREEK,55,Field Inspection,13,9,,f9ccd885-1a91-497c-b1df-4818419373ac,

to these SQL insert statements:

    insert into small_waterloo_tree_inventory 
    (X, Y, OBJECTID, TREEID, CIVIC_NO, STREET, LOCATION, SPECIES_NAME, SPECIES_LATIN, SPECIES_CODE, LANDUSE, ROADSEGMENTID, PARK, WARD, PLANTED_BY, MONTH_PLANTED, YEAR_PLANTED, STOCK_TYPE, STOCK_SIZE, STATUS, STATUS_DATE, CREATE_BY, CREATE_DATE, CREATE_YEAR, CREATE_MONTH, UPDATE_BY, UPDATE_DATE, SOURCE, SOURCE_DATE, OWNERSHIP, CATEGORY, ROOT_PATHWAYS, SOIL_VOLUME_M3, INITIAL_ACCEPTANCE_DATE, FINAL_ACCEPTANCE_DATE, OVERHEAD_HYDRO, DEVELOPMENT_AGE, PLANNING_COMMUNITY, SUB_WATERSHED, MAP_DBH_CM, GIS_NOTES, HEIGHT_ESTM_LIDAR_2014_M, HEIGHT_ESTM_LIDAR_2019_M, TAG1, GLOBALID, INSPECTED_YEAR)
    values 
    (-80.5095189090518, 43.412175164406, 1, 10007057, 27, 'ACTIVA AVE', 'BOULEVARD', 'Autumn Brilliance Serviceberry', 'Amelanchier x grandiflora ''Autumn Brilliance''', 'AMGRAB', 'ROW', 40056, NULL, 5, 'CITY CONTRACTOR', 'NOVEMBER', 2014, 'BALL AND BURLAP', '50 mm', 'REMOVED', '2020/07/30 12:53:44+00', NULL, '2015/12/23 10:34:03+00', 2015, 'December', 'GIS_DATA', '2018/03/05 17:14:35+00', 'Tree Inventory', NULL, 'CITY', 'Small Tree', 'N', NULL, NULL, NULL, 'None', 1997, 'LAURENTIAN WEST', 'BORDEN CREEK', 7, 'ADAM BUITENDYK', 0, 10, NULL, '0a2719cc-94b2-42c7-80b7-5dc0c5fe0f24', NULL);

    insert into small_waterloo_tree_inventory 
    (X, Y, OBJECTID, TREEID, CIVIC_NO, STREET, LOCATION, SPECIES_NAME, SPECIES_LATIN, SPECIES_CODE, LANDUSE, ROADSEGMENTID, PARK, WARD, PLANTED_BY, MONTH_PLANTED, YEAR_PLANTED, STOCK_TYPE, STOCK_SIZE, STATUS, STATUS_DATE, CREATE_BY, CREATE_DATE, CREATE_YEAR, CREATE_MONTH, UPDATE_BY, UPDATE_DATE, SOURCE, SOURCE_DATE, OWNERSHIP, CATEGORY, ROOT_PATHWAYS, SOIL_VOLUME_M3, INITIAL_ACCEPTANCE_DATE, FINAL_ACCEPTANCE_DATE, OVERHEAD_HYDRO, DEVELOPMENT_AGE, PLANNING_COMMUNITY, SUB_WATERSHED, MAP_DBH_CM, GIS_NOTES, HEIGHT_ESTM_LIDAR_2014_M, HEIGHT_ESTM_LIDAR_2019_M, TAG1, GLOBALID, INSPECTED_YEAR)
    values 
    (-80.4806046253164, 43.4464481686235, 2, 153401, 10, 'CAMERON ST N', 'LAWN', 'Norway Maple', 'Acer platanoides', 'ACPL', 'ROW', 11547, NULL, 10, 'UNKNOWN', 'UNKNOWN', 0, 'UNKNOWN', 'UNKNOWN', 'ACTIVE', '2017/01/31 15:14:06+00', 'Mark Grondin', '2009/10/17 00:00:00+00', 2009, 'October', 'Esri_Anonymous', '2017/01/31 20:14:06+00', 'Tree Inventory', '2009/10/17 00:00:00+00', 'CITY', 'Maple_Norway', 'N', NULL, NULL, NULL, 'Three phase', 1908, 'KING EAST', 'UPPER SCHNEIDER CREEK', 55, 'Field Inspection', 13, 9, NULL, 'f9ccd885-1a91-497c-b1df-4818419373ac', NULL);

To use Rome while I'm learning how to cross-compile a Rust app to multiple operating systems, please clone the repository locally and compile it from source:

    $ git clone https://github.com/htmfilho/roma.git
    $ cd roma
    $ git fetch origin 0.1.0
    $ git checkout tags/0.1.0 -b 0.1.0
    $ cargo build --release
    $ cargo install --path .

Roma is now ready to run:

    $ roma --csv waterloo_tree_inventory.csv

The output is the file `waterloo_tree_inventory.sql` in the same folder, with all insert statements.

In future releases, you will be able to:

- change column separator to tab.

- attach a prefix and a suffix content from other files.

- set a table name different from the file name.

- set the column names and their types different from the headers.

- create insert statements that insert multiple records.

- wrap multiple insert statements within a transaction scope.

But we are not limited to these. Let us know if you have any special needs by [creating an issue](https://github.com/htmfilho/roma/issues) in our repository.

Rust is definitely complicated. It took me a month to write the equivalent code that I wrote in 3 days in Go. The code might be memory safe, but I wouldn't use the adjective "correct" like many Bloggers and Youtubers out there. A runtime panic exception is an evidence that correctness depends on the programmer, not the language. I still believe that Go is better than Rust, but it is delightful to see a Rust application running, using very minimal resources.