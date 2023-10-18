-- lists all comedy shows in a particular database

SELECT tv_show.`title`
    FROM `tv_shows` AS tv_show
        INNER JOIN `tv_show_genres` AS state
        ON tv_show.`id` = state.`show_id`

        INNER JOIN `tv_genres` AS genre
        ON genre.`id` = state.`genre_id`
        WHERE genre.`name` = 'Comedy'
    ORDER BY tv_show.`title`
