DROP TABLE IF EXISTS mart_daily_counts;

CREATE TABLE mart_daily_counts AS
SELECT
    DATE(loaded_at) AS day,
    COUNT(*) AS record_count
FROM stg_events
GROUP BY DATE(loaded_at)
ORDER BY day;
