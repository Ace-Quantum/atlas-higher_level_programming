-- only list records with a name

SELECT score, name
FROM second_table
WHERE name IS NOT null
ORDER BY score DESC;