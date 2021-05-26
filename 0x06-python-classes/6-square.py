#!/usr/bin/python3
'''
Module of a Square class
'''


class Square:
    '''A simple class that defines a square
    Attributes:
        size(int): The size of the square
        position(tuple int): The position of the square
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialization method for the Square class
        Args:
            size(int): The size of the square
            position(tuple int): The position of the square
        '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''The getter function for the size attribute
        Returns:
            size
        '''
        return self.__size

    @size.setter
    def size(self, val):
        '''The setter function for the size attribute
        Args:
            value: The value to be set as the size
        '''
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    @property
    def position(self):
        '''The getter function for the position attribute
        Returns:
            The position tuple
        '''
        return self.__position

    @position.setter
    def position(self, val):
        '''The setter function for the position attribute
        Args:
            value: The position tuple
        '''
        if isinstance(val, tuple) and len(val) == 2:
            if isinstance(val[0], int) and isinstance(val[1], int):
                if val[0] >= 0 and val[1] >= 0:
                    self.__position = val
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        '''Finds the area of the Square
        Returns:
            The area of the square
        '''
        return self.__size ** 2

    def my_print(self):
        '''Prints the square using "#"
        '''
        if self.size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
