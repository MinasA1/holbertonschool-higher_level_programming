#!/usr/bin/python3
"""my filter states"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    import re

    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    cur = db.cursor()
    inp = re.search("\w+", sys.argv[4])
    cur.execute("SELECT * FROM states WHERE name = '{}'".format(inp.group(0)))
    for row in cur.fetchall():
        print(row)
    db.close()
