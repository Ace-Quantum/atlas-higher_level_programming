-- lists cities by states I'm assuming

SELECT cities.id, DISTINCT cities.name, states.name
FROM cities, states
ORDER BY cities.id ASC
;