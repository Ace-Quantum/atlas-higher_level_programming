-- lists cities by states I'm assuming

SELECT cities.id, cities.name, states.name
FROM cities
ORDER BY cities.id ASC;