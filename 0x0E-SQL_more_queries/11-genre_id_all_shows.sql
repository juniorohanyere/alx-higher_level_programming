-- script that lists all shows contained in the database

SELECT state.`title`, genre.`genre_id`
    FROM `tv_shows` AS state
        LEFT JOIN `tv_show_genres` AS genre
        ON state.`id` = genre.`show_id`
    ORDER BY state.`title`, genre.`genre_id`;
