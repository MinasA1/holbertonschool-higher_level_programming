#!/usr/bin/python3
"""my filter states"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect("localhost", sys.argv[1],
                         sys.argv[2], sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name" +
                " FROM cities INNER JOIN states" +
                " ON cities.state_id = states.id")
    for row in cur.fetchall():
        print(row)
    db.close()
