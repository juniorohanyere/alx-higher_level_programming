-- script that uses a database to list all genres of a show

SELECT genre.`name`
    FROM `tv_genres` AS genre
        INNER JOIN `tv_show_genres` AS state
        ON genre.`id` = state.`genre_id`

        INNER JOIN `tv_shows` AS tv_show
        ON tv_show.`id` = state.`show_id`
        WHERE tv_show.`title` = 'Dexter'
    ORDER BY genre.`name`;
