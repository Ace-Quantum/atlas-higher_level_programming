#!/usr/bin/python3

"""
Here is a script to list states by IDs
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("""
    SELECT id, name 
    FROM states
    WHERE name = '{}'
    ORDER BY states.id ASC;""".format(sys.argv[4]))
    
    results = cur.fetchall()

    for state in results:
        print(state)