#!/usr/bin/env python3
"""list all using SQLAlchemy"""
import sys
import re
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
    state = State(name="Louisiana")
    Session.add(state)
    Session.commit()
    print(state.id)
