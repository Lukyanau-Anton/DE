CREATE DATABASE IF NOT EXISTS service_catalogs;
-- ENGINE = PostgreSQL('postgres', 'analytics', 'user', 'user', 'service_catalogs', 0);
-- CREATE TABLE analytics.receipts_items
-- (
--     item_id UInt64,
--     mark_id UInt64,
--     sold_at DateTime('Europe/Minsk'),
--     gtin    String
-- ) ENGINE = MergeTree ORDER BY (item_id) SETTINGS index_granularity = 8192;