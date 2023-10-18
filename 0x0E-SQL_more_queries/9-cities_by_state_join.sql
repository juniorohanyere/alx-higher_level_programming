-- list all cities contained in a given database

SELECT city.`id`, city.`name`, state.`name`
    FROM `cities` AS city
        INNER JOIN `states` AS state
        ON city.`state_id` = city.`id`
    ORDER BY city.`id`;
