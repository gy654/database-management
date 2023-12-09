-- TODO: use explain / analyze, create an index
-- 1. Drop an existing index:

drop index if exists athlete_event_name_idx;

-- 2. Write a simple query: 
-- write a query to find all rows that contain the athlete Michael Fred Phelps, II (use the name column), display all columns

select * from athlete_event
where name = 'Michael Fred Phelps, II';

-- 3. Using EXPLAIN ANALYZE:
-- Rewrite your query, but prefix with EXPLAIN ANALYZE to show how much time it takes to run your query, include the output of the query in a comment beneath your EXPLAIN ANALYZE statement

explain analyze select * from athlete_event
where name = 'Michael Fred Phelps, II';

-- output
```
"QUERY PLAN"
"Gather  (cost=1000.00..8218.46 rows=54 width=136) (actual time=59.377..62.071 rows=30 loops=1)"
"  Workers Planned: 2"
"  Workers Launched: 2"
"  ->  Parallel Seq Scan on athlete_event  (cost=0.00..7213.06 rows=22 width=136) (actual time=43.165..47.614 rows=10 loops=3)"
"        Filter: (name = 'Michael Fred Phelps, II'::text)"
"        Rows Removed by Filter: 90362"
"Planning Time: 0.082 ms"
"Execution Time: 62.095 ms"

```

-- 4. Add an index:
-- write a query to add an index to the name column of the athlete_event table, make sure to name your index athlete_event_name_idx

create index athlete_event_name_idx on athlete_event (name);

-- 5. Verifying improved performance:
-- repeat your EXPLAIN ANALYZE query from (3), again, include the output of the query in a comment beneath your EXPLAIN ANALYZE statement, 
-- this time, the output should look like this – note that a Seq Scan is not used, and instead, an Index Scan is used (meaning that the query planner used the index to find the rows more quickly):

explain analyze select * from athlete_event
where name = 'Michael Fred Phelps, II';

-- output:
```

"QUERY PLAN"
"Bitmap Heap Scan on athlete_event  (cost=4.84..205.89 rows=54 width=136) (actual time=3.605..3.614 rows=30 loops=1)"
"  Recheck Cond: (name = 'Michael Fred Phelps, II'::text)"
"  Heap Blocks: exact=2"
"  ->  Bitmap Index Scan on athlete_event_name_idx  (cost=0.00..4.83 rows=54 width=0) (actual time=0.061..0.062 rows=30 loops=1)"
"        Index Cond: (name = 'Michael Fred Phelps, II'::text)"
"Planning Time: 0.590 ms"
"Execution Time: 3.657 ms"

```

-- 6. Ignoring an index:
-- write a query using the name column in the where clause, try to come up with some other operation or filter so that the index is not used (that is, an Index Scan is not used)

select * from athlete_event
where sex = 'M' and name ilike 'Christine%';