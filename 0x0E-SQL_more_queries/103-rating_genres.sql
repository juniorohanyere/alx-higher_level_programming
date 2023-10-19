-- lists all genres in a database by their rating.

SELECT `name`, SUM(`rate`) AS `rating`
    FROM `tv_genres` AS genre
        INNER JOIN `tv_show_genres` AS state
        ON state.`genre_id` = genre.`id`

        INNER JOIN `tv_show_ratings` AS r
        ON r.`show_id` = state.`show_id`

   GROUP BY `name`
   ORDER BY `rating` DESC;
