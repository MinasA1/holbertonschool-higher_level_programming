#!/usr/bin/python3
"""my filter states"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2],
                         sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM " +
                "cities INNER JOIN states ON cities.state_id = states.id" +
                " WHERE states.name='{}'".format(sys.argv[4]))
    cities = []
    for row in cur.fetchall():
        cities.append(''.join(row))
    for i, j in enumerate(cities):
        print(j, end=", " if i < len(cities)-1 else"\n")
    db.close()
