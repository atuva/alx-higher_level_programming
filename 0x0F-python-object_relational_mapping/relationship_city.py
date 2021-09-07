#!/usr/bin/python3
'''
Contains a class state and and instance of declarative_base() from sqlalchemy
'''
from sqlalchemy import Integer, String, Column, ForeignKey
from relationship_state import Base


class City(Base):
    '''A model for the city that links to a table cities on the db server
    Has a one to many relationship with states
    Attributes:
        id(int): An auto generated unique integer, can't be null and is a pk
        name(str): The name of the state, max 128 chars and can't be null
        state_id(int): Foreign key to states.id can't be null
    '''
    __tablename__ = 'cities'
    id = Column(Integer(), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
