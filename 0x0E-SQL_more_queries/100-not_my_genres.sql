-- script that uses the hbtn_0d_tvshows database to list all genres not linked
-- to the show Dexter

SELECT DISTINCT `name`
    FROM `tv_genres` AS genre
        INNER JOIN `tv_show_genres` AS state
            ON genre.`id` = state.`genre_id`

        INNER JOIN `tv_shows` AS tv_show
        ON state.`show_id` = tv_show.`id`

        WHERE genre.`name` NOT IN (
            SELECT `name`
                FROM `tv_genres` AS genre
                    INNER JOIN `tv_show_genres` AS state
                    ON genre.`id` = state.`genre_id`

                    INNER JOIN `tv_shows` AS tv_show
                    ON state.`show_id` = tv_show.`id`

                    WHERE tv_show.`title` = 'Dexter'
            )

    ORDER BY genre.`name`;
