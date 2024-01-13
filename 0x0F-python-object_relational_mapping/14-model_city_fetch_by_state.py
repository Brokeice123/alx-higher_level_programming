#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(City, State).filter(City.state_id == State.id).all()
    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
