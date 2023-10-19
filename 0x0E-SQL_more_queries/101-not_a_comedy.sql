-- lists all shows without the comedy genre in a database

SELECT DISTINCT `title`
    FROM `tv_shows` AS tv_show
        LEFT JOIN `tv_show_genres` AS state
        ON state.`show_id` = tv_show.`id`

        LEFT JOIN `tv_genres` AS genre
        ON genre.`id` = state.`genre_id`
        WHERE tv_show.`title` NOT IN
            (SELECT `title`
                FROM `tv_shows` AS tv_show
	            INNER JOIN `tv_show_genres` AS state
		    ON state.`show_id` = tv_show.`id`

		    INNER JOIN `tv_genres` AS genre
		    ON genre.`id` = state.`genre_id`

                    WHERE genre.`name` = "Comedy")
    ORDER BY `title`;
