#!/usr/bin/env python3
"""list all using SQLAlchemy"""
import sys
import sqlalchemy
if __name__ == "__main__":
    inp = "mysql://{}:{}@localhost:3306/{}".format(sys.argv[1],
                                                   sys.argv[2],
                                                   sys.argv[3],)
    eng = sqlalchemy.create_engine(inp)
    connect = eng.connect()
    states = eng.execute("SELECT cities.id, cities.name, states.name"+
                " FROM cities INNER JOIN states"+
                " ON cities.state_id = states.id")
    print("\n".join(["{}: ({}) {}".format(col[2], col[0], col[1]) for col in states]))
    connect.close()
