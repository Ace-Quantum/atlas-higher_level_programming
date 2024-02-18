-- counts how many shows are in each genre

SELECT tv_show_genres.name AS Genra, 
COUNT(tv_show_genres.name) AS number_of_shows
FROM tv_genres
NATURAL JOIN tv_show_genres
ON tv_show_genres.id = tv_genres.genra_id
WHERE number_of_shows > 0;