-- lists all shows, and all genres linked to that particular show, from a
-- particular database

SELECT tv_show.`title`, genre.`name`
    FROM `tv_shows` AS tv_show
        LEFT JOIN `tv_show_genres` AS state
        ON tv_show.`id` = state.`show_id`

        LEFT JOIN `tv_genres` AS genre
        ON state.`genre_id` = genre.`id`
    ORDER BY tv_show.`title`, genre.`name`;
