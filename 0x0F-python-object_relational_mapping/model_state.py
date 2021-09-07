#!/usr/bin/python3
'''
Contains a class state and and instance of declarative_base() from sqlalchemy
'''
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''A model for the states that links to a table states on the db server
    Attributes:
        id(str): An auto generated unique integer, can't be null and is a pk
        name(str): The name of the state, max 128 chars and can't be null
    '''
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
