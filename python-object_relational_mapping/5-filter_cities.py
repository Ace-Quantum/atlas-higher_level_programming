#!/usr/bin/python3

"""
Here is a script to list all cities in a state
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    state_name_var = sys.argv[4].replace("'", "")

    cur.execute("""
    SELECT cities.name 
    FROM cities
    INNER JOIN states
    ON cities.state_id = states.id
    WHERE states.name = '{}'
    ORDER BY states.id ASC;""".format(state_name_var))
    
    results = cur.fetchall()

    cities_results = []

    for result in results:
        cities_results.append(result[0])

    print(", ".join(cities_results))

    # for state in results:
        # print(results[0], end=", ")

    cur.close()
    db.close()