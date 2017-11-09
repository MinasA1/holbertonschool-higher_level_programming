#!/usr/bin/env python3
"""filter states"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    cur = db.cursor()
    cur.execute( "SELECT * FROM states WHERE name REGEXP '^[N]'" )
    for row in cur.fetchall():
        print(row)
    db.close()
