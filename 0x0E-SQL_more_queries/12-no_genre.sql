-- lists all shows contained in a particular database without a genre linked

SELECT state.`title`, genre.`genre_id`
    FROM `tv_shows` AS state
        LEFT JOIN `tv_show_genres` AS genre
        ON state.`id` = genre.`show_id`
        WHERE genre.`genre_id` IS NULL
    ORDER BY state.`title`, genre.`genre_id`;
