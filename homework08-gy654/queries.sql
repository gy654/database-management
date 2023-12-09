-- TODO: write the task number and description followed by the query
-- Task 1. Write a View

drop view if exists ath_reg;
create or replace view ath_reg as
select athlete_event_id, id, name,  height, weight, athlete_event.noc, team, year,  sport, event, 
	medal,(case when region is null and noc_region.noc = 'SGP' then 'Singapore'
	when region is null and team = 'ROT' then 'Refugee'
	when region is null and team = 'TUV' then 'Tuvalu'
	when region is null and team = 'UNK' then 'Unknown'
	when region is null then team
	else region end) as region 
from athlete_event
left join noc_region
on athlete_event.noc = noc_region.noc
where medal is not null;

select * from ath_reg;

-- Task 2. Use the Window Function, rank()
-- Show the top 3 ranked regions for each fencing 🤺 event based on the number of total gold medals 🥇 that region had for that fencing event:
with fencing_gold_medal_rank as(
	select region, event, count(*) as gold_medals, rank() over (partition by event order by count(*) desc) as rank
	from ath_reg
	where event ilike 'fencing%' and medal = 'Gold'
	group by 1, 2
	order by event)
select * from fencing_gold_medal_rank where rank <=3;

-- 3. Using Aggregate Functions as Window Functions: 
-- Show the rolling sum of medals per region, per year, and per medal type.

select region, year, medal, count(medal) as c, 
		sum(count(medal))over (partition by region, medal order by region, year, medal) as sum
	from ath_reg
	group by 1,2,3
	order by 1,2,3;

-- 4. Use the Window Function, lag()
-- Show the height of every gold medalist for pole valut events, along with the height of the gold medalist for that same pole value event in the previous year.


select event,year, height,
	lag(height, 1) over (order by event, year) as previous_height
from ath_reg
where event ilike '%pole vault' and medal = 'Gold'
order by event, year;
