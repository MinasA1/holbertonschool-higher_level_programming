#!/usr/bin/env python3
"""my filter states"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2],
                         sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'".format(sys.argv[4]))
    for row in cur.fetchall():
        print(row)
    db.close()
