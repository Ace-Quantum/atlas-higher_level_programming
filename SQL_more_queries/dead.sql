-- counts how many shows are in each genre

SELECT tv_genres.name AS Genre, 
COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_show_genres.genre_id;
-- WHERE number_of_shows > 0;