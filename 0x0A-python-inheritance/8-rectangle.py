#!/usr/bin/python3
'''
Module contains empty class
'''


class BaseGeometry:
    '''
    An empty class BaseGeometry
    '''

    def area(self):
        '''
        Empty area method
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''
        Validates integers
        Args:
            name (str): The name
            value (int): An integer value
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''
    A rectangle class
    '''
    def __init__(self, width, height):
        '''
        args:
            width (int): Width of rectangle
            height (int): Height of rectangle
        '''
        self.integer_validator("Width", width)
        self.__width = width
        self.integer_validator("Height", height)
        self.__height = height
