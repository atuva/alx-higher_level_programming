#!/usr/bin/python3
"""Contains a script that lists all State objects from the database
"""
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, Session

if __name__ == "__main__":
    eng = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True)

    engine = create_engine(eng)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    query = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()

    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
