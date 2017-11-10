#!/usr/bin/python3
"""list all using SQLAlchemy"""
import sys
import sqlalchemy
if __name__ == "__main__":
    inp = "mysql://{}:{}@localhost:3306/{}".format(sys.argv[1],
                                                   sys.argv[2],
                                                   sys.argv[3],)
    eng = sqlalchemy.create_engine(inp)
    connect = eng.connect()
    states = eng.execute("SELECT * FROM states " +
                         "ORDER BY states.id ASC")
    print("\n".join(["{}: {}".format(col[0], col[1]) for col in states]))
    connect.close()
