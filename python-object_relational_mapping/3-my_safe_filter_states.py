#!/usr/bin/python3

"""
Here is a script to list states by IDs
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )
    cur = db.cursor()

    state_name_var = sys.argv[4].replace("'", "")

    cur.execute(
        """
    SELECT id, name
    FROM states
    WHERE name = '{}'
    ORDER BY states.id ASC;""".format(
            state_name_var
        )
    )

    results = cur.fetchall()

    for state in results:
        print(state)
