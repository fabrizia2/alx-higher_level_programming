#!/usr/bin/python3

"""
changes the name of a State object from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    """
    Not to be executed when imported
    """

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]), echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.id == 2).first()

    result.name = "New Mexico"

    session.commit()