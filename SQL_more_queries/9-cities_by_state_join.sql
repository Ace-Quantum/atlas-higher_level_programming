-- lists cities by states I'm assuming

SELECT cities.id, cities.name, states.name
FROM cities, states
ORDER BY cities.id ASC
FETCH FIRST 1 ROWS ONLY;