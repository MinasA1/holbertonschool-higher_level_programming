#!/usr/bin/env python3
"""list all using SQLAlchemy"""
import sys
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from model_state import State
if __name__ == "__main__":
    inp = "mysql://{}:{}@localhost:3306/{}".format(sys.argv[1],
                                                   sys.argv[2],
                                                   sys.argv[3],)
    eng = sqlalchemy.create_engine(inp)
    session = sessionmaker(bind=eng)
    Session = session()
    for col in Session.query(State).filter(State.name.contains('a')):
        print("{}: {}".format(col.id, col.name))
