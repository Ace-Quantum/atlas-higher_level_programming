-- lists cities by states I'm assuming

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON state_id
ORDER BY cities.id ASC;