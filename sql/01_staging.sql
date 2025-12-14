DROP TABLE IF EXISTS stg_events;

CREATE TABLE stg_events AS
SELECT
    *,
    NOW() AS loaded_at
FROM raw_events;
