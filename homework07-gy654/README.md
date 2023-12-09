## Part1: Create an ER Diagram by inspecting tables

table `countries` has a one to many relationship with table `country_stats` since the column `country_id` in `country_stats` reference `country_id` in `countries`.

table `countries` has a many to one relationship with table `regions` since the column `region_id` in `regions` reference `region_id` in `countries`.

table `countries` has a one to many relationship with table `country_languages` since the column `country_id` in `country_languages` reference `country_id` in `countries`.

table `continents` has a one to many relationship with table `regions` since the column `continent_id` in `continents` reference `continent_id` in `regions`.

table `languages` has a one to many relationship with table `country_languages` since the column `language_id` in `languages` reference `language_id` in `country_languages`.



## Part3

interpreting the results of your queries underneath the pasted output:

-- 1. This query shows possible values of product_type

```
 product_type 
--------------
 CONCOMITANT
 SUSPECT
(2 rows)
```

-- 2. this query shows the composite primary key is (report_id, product, product_type, product_code)
```
 count 
-------
(0 rows)
```


-- 3. This query shows columns that are dependent solely on report_id:
-- caers_created_date, date_event,  patient_age, age_unites, sex, case_meddra_preferred_terms, case_outcome

``` 
report_id 
-----------
(0 rows)
```

-- 4. this query shows that description is solely dependent on product code
``` 
product_code 
--------------
(0 rows)
```

## Part4

![image info](./part3_er_diagram.png)

- Table1 `report_product` contains 4 attributes:
    - `report_id`
    - `product_type`
    - `product`
    - `product_code`
    
    the composite primary key of the table is all of the columns so that the third nomalized form is satisfied

- Table2 `report` contains 8 attributes:
    - `report_id`
    - `caers_created_date`
    - `date_event`
    - `patient_age`
    - `age_unite`s
    - `sex`
    - `case_meddra_preferred_terms`
    - `case_outcome`

    The primary key of the table is report_id
    The foreign key is report_id which references Table1 `report_product`

- Table3 `product` contains 2 attributes:
    - `product_code`
    - `description`

    The primary key of the table is product_code
    The foreign key is product_code which references Table1 `report_product`

Each table is now in the third normal form. All the attributes in a table are functionally dependent on solely the whole set of primary key.