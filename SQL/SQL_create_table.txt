CREATE TABLE IF NOT EXISTS fact_pageviews (
    article TEXT NOT NULL,
    views BIGINT,
    language VARCHAR(10),
    platform TEXT,
    datetime TIMESTAMP NOT NULL
) PARTITION BY RANGE (datetime);

create TABLE fact_pageviews_day1 PARTITION OF fact_pageviews
    FOR VALUES FROM ('2026-03-01 00:00:00') TO ('2026-03-02 00:00:00');

create TABLE fact_pageviews_day2 PARTITION OF fact_pageviews
    FOR VALUES FROM ('2026-03-02 00:00:00') TO ('2026-03-03 00:00:00');

create TABLE fact_pageviews_day3 PARTITION OF fact_pageviews
    FOR VALUES FROM ('2026-03-03 00:00:00') TO ('2026-03-04 00:00:00');

create TABLE fact_pageviews_day4 PARTITION OF fact_pageviews
    FOR VALUES FROM ('2026-03-04 00:00:00') TO ('2026-03-05 00:00:00');

create TABLE fact_pageviews_day5 PARTITION OF fact_pageviews
    FOR VALUES FROM ('2026-03-05 00:00:00') TO ('2026-03-06 00:00:00');

create TABLE fact_pageviews_day6 PARTITION OF fact_pageviews
    FOR VALUES FROM ('2026-03-06 00:00:00') TO ('2026-03-07 00:00:00');
	
create TABLE fact_pageviews_day7 PARTITION OF fact_pageviews
    FOR VALUES FROM ('2026-03-07 00:00:00') TO ('2026-03-08 00:00:00');

create TABLE fact_pageviews_default PARTITION OF fact_pageviews DEFAULT;


