with cte as (
  SELECT article,
  views,
  round((views - views_lag)::numeric / views_lag, 2) as views_diff,
  datetime
  FROM lag_views_table
  where views_lag > 500 
  and views > 500
  and datetime - datetime_lag = interval '1 hour' 
  and article != 'Main_Page')
  
select article, max(views_diff) as growth_Rate
from cte
where $__timeFilter(datetime) 
group by article
order by max(views_diff) desc;

select sum(views) as views, language
from fact_pageviews
where $__timeFilter((datetime))
group by language
order by sum(views) desc
limit 10;

select sum(views) as views, datetime
from fact_pageviews
GROUP BY datetime;

select sum(views) as views, article
from fact_pageviews
where $__timeFilter((datetime)) 
and article != 'Main_Page'
group by md5(article), article
order by sum(views) desc
limit 10;

SELECT 
SUM(views) AS "views",  
platform 
FROM fact_pageviews
WHERE language = 'ru'
GROUP BY language, platform;





