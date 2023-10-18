-- script that creates a new database table on a MySQL server

CREATE TABLE IF NOT EXISTS `unique_id` (
    `id`    INT DEFAULT 1   UNIQUE,
    `name`  VARCHAR(256)
);
