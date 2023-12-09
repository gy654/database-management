-- write your queries underneath each number:
 
-- 1. the total number of rows in the database
select count(*) from accident;
-- 2. show the first 15 rows, but only display 3 columns (your choice)
select collision_id, crash_date, borough from accident limit 15;
-- 3. do the same as above, but chose a column to sort on, and sort in descending order
select collision_id, crash_date, borough from accident order by collision_id desc limit 15;
-- 4. add a new column without a default value
alter table accident add number_person_killed_and_injured int;
-- 5. set the value of that new column
update accident alter column number_person_killed and injured set default 0;
-- 6. show only the unique (non duplicates) of a column of your choice
select distinct borough from accident;
-- 7.group rows together by a column value (your choice) and use an aggregate function to calculate something about that group 
select borough, count(borough) as num_accident from accident group by borough;
-- 8. now, using the same grouping query or creating another one, find a way to filter the query results based on the values for the groups 
select borough, count(borough) as num_accident from accident group by borough having count(borough) > 10000;
-- 9. examine the number of accident happening in each hour during the day.
select extract(hour from crash_time) as accident_hour, count(extract(hour from crash_time)) as hour_count from accident group by extract(hour from crash_time) order by accident_hour;
-- 10. examine which accident has the most number of persons killed
select collision_id, number_of_persons_killed from accident where number_of_persons_killed =(select max(number_of_persons_killed) from accident);
-- 11. examine the number of accident happening in each moth during the year
select extract(month from crash_date) as accident_month, count(extract(month from crash_date)) as month_count from accident group by extract(month from crash_date)  order by accident_month;
-- 12. examine top 5 vehicle types code 1 with most number of accidents
select vehicle_type_code_1, count(vehicle_type_code_1) as vehicle_count from accident group by vehicle_type_code_1 order by vehicle_count desc limit 5;

