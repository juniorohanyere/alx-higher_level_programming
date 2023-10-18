-- lists all genres from a particular database and displays all shows linked

SELECT genre.`name` AS `genre`,
    COUNT(*) AS `number_of_shows`
    FROM `tv_genres` AS genre
        INNER JOIN `tv_show_genres` AS tv_show
        ON genre.`id` = tv_show.`genre_id`
    GROUP BY genre.`name`
    ORDER BY `number_of_shows` DESC;
