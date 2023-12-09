# Overview

* Format: csv
* Size: 14.73 MB
* Number of Records: 74881 
* Name / Title: NYC Traffic Accidents
* Link to Data: https://www.kaggle.com/datasets/mysarahmadbhat/nyc-traffic-accidents?resource=download
* Source / Origin: 
	* Author or Creator: MYSAR AHMAD BHAT
	* Publication Date: 2020.09
	* Publisher: NYC OpenData
	* Version or Data Accessed: 1
* License: CC0: Public Domain
* Can You Use this Data Set for Your Intended Use Case? yes

## Fields or Column Headers

* Column 1: crash date, object 
* Column 2: crash time, object
* Column 3: borough, object
* Column 4: zip code,float64
* Column 5: latitude, float64
* Column 6: longitude, float64
* Column 7: location, object 
* Column 8: on street name, object 
* Column 9: cross street name, object 
* Column 10: off street name, object 
* Column 11: number of persons injured, int64 
* Column 12: number of persons killed, int64 
* Column 13: number of pedestrians injured, int64 
* Column 14: number of pedestrians killed, int64 
* Column 15: number of cyclist injured,int64 
* Column 16: number of cyclist killed, int64 
* Column 17: number of motorist injured, int64 
* Column 18: number of motorist killed, int64 
* Column 19: contributing factor vehicle 1, object
* Column 20: contributing factor vehicle 2, object
* Column 21: contributing factor vehicle 3, object
* Column 22: contributing factor vehicle 4, object
* Column 23: contributing factor vehicle 5, object
* Column 24: collision_id, int64  
* Column 25: vehicle type code 1, object
* Column 26: vehicle type code 2, object
* Column 27: vehicle type code 3, object
* Column 28: vehicle type code 4, object
* Column 29: vehicle type code 5, object


# Table Design

- The primary key for the dataset is `collision_id`


2. My decisions for each field :

| column index 	| column name                   	| data type 	| null values 	| duplicates 	| default values 	|
|--------------	|-------------------------------	|-----------	|-------------	|------------	|----------------	|
| 0            	| crash_date                    	| TIMESTAMP 	|             	| 74639      	|                	|
| 1            	| crash_time                    	| TIME      	|             	| 73441      	|                	|
| 2            	| borough                       	| VARCHAR   	| NaN         	| 74875      	|                	|
| 3            	| zip_code                      	| CHAR      	| NaN         	| 74682      	|                	|
| 4            	| latitude                      	| FLOAT     	| NaN         	| 45774      	|                	|
| 5            	| longitude                     	| FLOAT     	| NaN         	| 51328      	|                	|
| 6            	| location                      	| VARCHAR   	| NaN         	| 38131      	|                	|
| 7            	| on_street_name                	| VARCHAR   	| NaN         	| 70871      	|                	|
| 8            	| cross_street_name             	| VARCHAR   	| NaN         	| 70475      	|                	|
| 9            	| off_street_name               	| VARCHAR   	| NaN         	| 57429      	|                	|
| 10           	| number_of_persons_injured     	| INT       	|             	| 74869      	|                	|
| 11           	| number_of_persons_killed      	| INT       	|             	| 74876      	|                	|
| 12         	| number_of_pedestrians_injured 	| INT       	|             	| 74875      	|                	|
| 13           	| number_of_pedestrians_killed  	| INT       	|             	| 74879      	|                	|
| 14           	| number_of_cyclist_injured     	| INT       	|             	| 74877      	|                	|
| 15           	| number_of_cyclist_killed      	| INT       	|             	| 74879      	|                	|
| 16           	| number_of_motorist_injured    	| INT       	|             	| 74869      	|                	|
| 17          	| number_of_motorist_killed     	| INT       	|             	| 74876      	|                	|
| 18           	| contributing_factor_vehicle_1 	| VARCHAR   	| NaN         	| 74825      	|                	|
| 19           	| contributing_factor_vehicle_2 	| VARCHAR   	| NaN         	| 74835      	|                	|
| 20           	| contributing_factor_vehicle_3 	| VARCHAR   	| NaN         	| 74851      	|                	|
| 21           	| contributing_factor_vehicle_4 	| VARCHAR   	| NaN         	| 74868      	|                	|
| 22          	| contributing_factor_vehicle_5 	| VARCHAR   	| NaN         	| 74874      	|                	|
| 23           	| collision_id                  	| INT       	|             	| 0          	|                	|
|  24         	| vehicle_type_code_1           	| VARCHAR   	| NaN         	| 74608      	|                	|
|  25         	| vehicle_type_code_2           	| VARCHAR   	| NaN         	| 74590      	|                	|
|  26         	| vehicle_type_code_3           	| VARCHAR   	| NaN         	| 74831      	|                	|
|  27          	| vehicle_type_code_4           	| VARCHAR   	| NaN         	| 74854      	|                	|
| 28          	| vehicle_type_code_5           	| VARCHAR   	| NaN         	| 74864      	|                	|

We do not need to specify the default value for any of the columns since there is no missing values in the csv. Allow nulls in all columns except for the primary key. All nulls are already marked as NaN.

3. write the actual SQL to make this table, and put it into your create_table.sql 
- prior to the CREATE TABLE statement, make sure to try to DROP the table first, but only if it exists
- make sure that the appropriate constraints are set (NOT NULL, UNIQUE, etc.)
- use descriptive names for the table and columns
- make sure all names are lowercase and separated with underscore

```
drop table if exists accident ;
create table accident (
    crash_date timestamp,
    crash_time time,
    borough varchar(255),
    zip_code char(10),
    latitude varchar(255),
    longitude varchar(255),
    loc varchar(255),
    on_street_name varchar(255),
    cross_street_name varchar(255),
    off_street_name varchar(255),
    number_of_persons_injured int,
    number_of_persons_killed int,
    number_of_pedestrians_injured int,
    number_of_pedestrians_killed int,
    number_of_cyclist_injured int,
    number_of_cyclist_killed int,
    number_of_motorist_injured int,
    number_of_motorist_killed int,
    contributing_factor_vehicle_1 varchar(255),
    contributing_factor_vehicle_2 varchar(255),
    contributing_factor_vehicle_3 varchar(255),
    contributing_factor_vehicle_4 varchar(255),
    contributing_factor_vehicle_5 varchar(255),
    collision_id int not null unique primary key,
    vehicle_type_code_1 varchar(255),
    vehicle_type_code_2 varchar(255),
    vehicle_type_code_3 varchar(255),
    vehicle_type_code_4 varchar(255),
    vehicle_type_code_5 varchar(255));
```

# Import

- I had an error during import: 
```
ERROR:  invalid input syntax for type double precision: ""
CONTEXT:  COPY accident, line 51, column latitude: ""
```
- How I fix this: I modified the create table query and set the data type of latitude and longitude as varchar(255) rather than float.

# Database Information

1. show all of databases in your postgres instance

```
query: \l
output:

                                             List of databases
    Name    |  Owner   | Encoding |   Collate   |    Ctype    | ICU Locale | Locale Provider |   Access privileges   
------------+----------+----------+-------------+-------------+------------+-----------------+-----------------------
 homework06 | yge      | UTF8     | en_US.UTF-8 | en_US.UTF-8 | en-US      | icu             | 
 postgres   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | en-US      | icu             | 
 template0  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | en-US      | icu             | =c/postgres          +
            |          |          |             |             |            |                 | postgres=CTc/postgres
 template1  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | en-US      | icu             | =c/postgres          +
            |          |          |             |             |            |                 | postgres=CTc/postgres
 yge        | yge      | UTF8     | en_US.UTF-8 | en_US.UTF-8 | en-US      | icu             | 
(5 rows)
```

2. (making sure you're connected to homework06 database) show all of the tables in your database

```
query: \dt
output:

         List of relations
 Schema |   Name   | Type  | Owner 
--------+----------+-------+-------
 public | accident | table | yge
(1 row)
```


3. finally, show some information about the table you created and imported data into: find a way to show its columns, types and constraints (hint: describe the table)

```
query: \d+ accident;
output:


                                                              Table "public.accident"
            Column             |            Type             | Collation | Nullable | Default | Storage  | Compression | Stats target | Description 
-------------------------------+-----------------------------+-----------+----------+---------+----------+-------------+--------------+-------------
 crash_date                    | timestamp without time zone |           |          |         | plain    |             |              | 
 crash_time                    | time without time zone      |           |          |         | plain    |             |              | 
 borough                       | character varying(255)      |           |          |         | extended |             |              | 
 zip_code                      | character(10)               |           |          |         | extended |             |              | 
 latitude                      | character varying(255)      |           |          |         | extended |             |              | 
 longitude                     | character varying(255)      |           |          |         | extended |             |              | 
 loc                           | character varying(255)      |           |          |         | extended |             |              | 
 on_street_name                | character varying(255)      |           |          |         | extended |             |              | 
 cross_street_name             | character varying(255)      |           |          |         | extended |             |              | 
 off_street_name               | character varying(255)      |           |          |         | extended |             |              | 
 number_of_persons_injured     | integer                     |           |          |         | plain    |             |              | 
 number_of_persons_killed      | integer                     |           |          |         | plain    |             |              | 
 number_of_pedestrians_injured | integer                     |           |          |         | plain    |             |              | 
 number_of_pedestrians_killed  | integer                     |           |          |         | plain    |             |              | 
 number_of_cyclist_injured     | integer                     |           |          |         | plain    |             |              | 
 number_of_cyclist_killed      | integer                     |           |          |         | plain    |             |              | 
 number_of_motorist_injured    | integer                     |           |          |         | plain    |             |              | 
 number_of_motorist_killed     | integer                     |           |          |         | plain    |             |              | 
 contributing_factor_vehicle_1 | character varying(255)      |           |          |         | extended |             |              | 
 contributing_factor_vehicle_2 | character varying(255)      |           |          |         | extended |             |              | 
 contributing_factor_vehicle_3 | character varying(255)      |           |          |         | extended |             |              | 
 contributing_factor_vehicle_4 | character varying(255)      |           |          |         | extended |             |              | 
 contributing_factor_vehicle_5 | character varying(255)      |           |          |         | extended |             |              | 
 collision_id                  | integer                     |           | not null |         | plain    |             |              | 
 vehicle_type_code_1           | character varying(255)      |           |          |         | extended |             |              | 
 vehicle_type_code_2           | character varying(255)      |           |          |         | extended |             |              | 
 vehicle_type_code_3           | character varying(255)      |           |          |         | extended |             |              | 
 vehicle_type_code_4           | character varying(255)      |           |          |         | extended |             |              | 
 vehicle_type_code_5           | character varying(255)      |           |          |         | extended |             |              | 
Indexes:
    "accident_pkey" PRIMARY KEY, btree (collision_id)
Access method: heap
```

# Query Results
```
### 1. the total number of rows in the database		
 count 
-------
 74881
(1 row)
```

```
### 2. show the first 15 rows, but only display 3 columns (your choice)	
collision_id |     crash_date      | borough  
--------------+---------------------+----------
      4342908 | 2020-08-29 00:00:00 | BRONX
      4343555 | 2020-08-29 00:00:00 | BROOKLYN
      4343142 | 2020-08-29 00:00:00 | 
      4343588 | 2020-08-29 00:00:00 | BRONX
      4342953 | 2020-08-29 00:00:00 | BROOKLYN
      4342721 | 2020-08-29 00:00:00 | 
      4343004 | 2020-08-29 00:00:00 | BRONX
      4343342 | 2020-08-29 00:00:00 | 
      4343030 | 2020-08-29 00:00:00 | BRONX
      4343040 | 2020-08-29 00:00:00 | QUEENS
      4342743 | 2020-08-29 00:00:00 | QUEENS
      4343448 | 2020-08-29 00:00:00 | QUEENS
      4343143 | 2020-08-29 00:00:00 | BRONX
      4343074 | 2020-08-29 00:00:00 | BROOKLYN
      4342716 | 2020-08-29 00:00:00 | 
(15 rows)
```

```
### 3. do the same as above, but chose a column to sort on, and sort in descending order

(sort by collision_id in descending order )

 collision_id |     crash_date      |  borough  
--------------+---------------------+-----------
      4343622 | 2020-08-29 00:00:00 | MANHATTAN
      4343621 | 2020-08-17 00:00:00 | MANHATTAN
      4343620 | 2020-08-27 00:00:00 | BROOKLYN
      4343619 | 2020-08-28 00:00:00 | 
      4343618 | 2020-08-28 00:00:00 | BRONX
      4343612 | 2020-08-26 00:00:00 | BROOKLYN
      4343610 | 2020-08-27 00:00:00 | BROOKLYN
      4343600 | 2020-08-24 00:00:00 | MANHATTAN
      4343599 | 2020-08-12 00:00:00 | 
      4343597 | 2020-08-28 00:00:00 | BRONX
      4343595 | 2020-08-28 00:00:00 | 
      4343594 | 2020-08-07 00:00:00 | MANHATTAN
      4343588 | 2020-08-29 00:00:00 | BRONX
      4343575 | 2020-08-27 00:00:00 | 
      4343569 | 2020-08-27 00:00:00 | MANHATTAN
(15 rows)
```

```
### 4. add a new column without a default value	
ALTER TABLE
```

```
### 5. set the value of that new column	
ALTER TABLE
```

```
### 6. show only the unique (non duplicates) of a column of your choice	
    borough    
---------------
 
 BRONX
 BROOKLYN
 MANHATTAN
 QUEENS
 STATEN ISLAND
(6 rows)
```

```
### 7.group rows together by a column value (your choice) and use an aggregate function to calculate something about that group 

group by borough and calculate the mean number of accident of each group.
    borough    | num_accident 
---------------+--------------
 STATEN ISLAND |         1446
 MANHATTAN     |         7353
 BRONX         |         9417
 QUEENS        |        14017
 BROOKLYN      |        16907
               |        25741
(6 rows)
```

```
### 8. now, using the same grouping query or creating another one, find a way to filter the query results based on the values for the groups 

filtering out boroughs where the number of accident >10000
 borough  | num_accident 
----------+--------------
 QUEENS   |        14017
 BROOKLYN |        16907
          |        25741
(3 rows)
```

```
### 9. examine the number of accident happening in each hour during the day.
accident_hour | hour_count 
---------------+------------
             0 |       2948
             1 |       1474
             2 |       1139
             3 |        989
             4 |        975
             5 |       1178
             6 |       1868
             7 |       2463
             8 |       3678
             9 |       3439
            10 |       3525
            11 |       3803
            12 |       4054
            13 |       4458
            14 |       5016
            15 |       4677
            16 |       5219
            17 |       4974
            18 |       4696
            19 |       3738
            20 |       3138
            21 |       2711
            22 |       2557
            23 |       2164
(24 rows)

```

```
### 10. examine which accident has the most number of persons killed	
collision_id | number_of_persons_killed 
--------------+--------------------------
      4278634 |                        4
(1 row)

```

```
### 11. examine the number of accident happening in each month during the year	
 accident_month | month_count 
----------------+-------------
              1 |       14287
              2 |       13684
              3 |       11057
              4 |        4116
              5 |        6149
              6 |        7616
              7 |        9225
              8 |        8747
(8 rows)
```

```
### 12. examine top 5 vehicle types code 1 with most number of accidents	
         vehicle_type_code_1         | vehicle_count 
-------------------------------------+---------------
 Sedan                               |         34349
 Station Wagon/Sport Utility Vehicle |         27541
 Taxi                                |          2768
 Pick-up Truck                       |          1882
 Box Truck                           |          1417
(5 rows)
```