-- lists cities by states I'm assuming

SELECT DISTINCT cities.id, cities.name, states.name
FROM cities, states
ORDER BY cities.id ASC;