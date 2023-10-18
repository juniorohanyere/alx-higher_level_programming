-- script that lists all shows contained in hbtn_0d_tvshows that have at least
-- one genre linked.

SELECT state.`title`, genre.`genre_id`
    FROM `tv_shows` AS state
        INNER JOIN `tv_show_genres` AS genre
        ON state.`id` = genre.`show_id`
    ORDER BY state.`title`, genre.`genre_id`;
