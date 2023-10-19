-- lists all shows from a database by their rating.

SELECT `title`, SUM(`rate`) AS `rating`
    FROM `tv_shows` AS tv_show
        INNER JOIN `tv_show_ratings` AS r
            ON tv_show.`id` = r.`show_id`
    GROUP BY `title`
    ORDER BY `rating` DESC;
