-- lists all cities that can be found in a specific database

SELECT `id`, `name`
    FROM `cities`
WHERE `state_id` IN (
    SELECT `id`
        FROM `states`
    WHERE `name` = 'California'
)
ORDER BY `id`;
