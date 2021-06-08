#!/usr/bin/python3
'''
This module contains the Base Class.
'''


class Base:
    '''
    The base of all the other classes in this project.
    It's main goal is to manage the id attribute in all future classes and to
    avoid duplicating the same code.

    Attributes:
        __nb_objects (int): A private class attribute
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Constrictor method for the class
        Args:
            id (int): The id of the instance
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
