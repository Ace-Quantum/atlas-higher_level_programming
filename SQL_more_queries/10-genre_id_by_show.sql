-- show genra by id

SELECT tv_shows.title, tv_show_genres.genre_id
WHERE tv_show_genres.genre_id IS NOT NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;