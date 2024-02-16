-- lists all cities from cali

SELECT name
FROM cities
WHERE state_id=
    (SELECT id
    FROM states
    WHERE name='california')
ORDER BY cities.id ASC;