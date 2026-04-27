create index idx_fact_pageviews_language 
ON fact_pageviews (language);

create index idx_fact_pageviews_platform 
ON fact_pageviews (platform);

create index idx_pageviews_language_platform 
ON fact_pageviews (language, platform);

CREATE index idx_fact_pageviews_datetime 
ON fact_pageviews (datetime);

create index idx_fact_pageviews_views ON fact_pageviews (views DESC);

CREATE index idx_fact_pageviews_article_views_sum 
ON fact_pageviews (article, views);

CREATE index idx_fact_pageviews_article_hash 
ON fact_pageviews (md5(article));
