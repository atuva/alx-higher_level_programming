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
        self.size = size
        self.position = position

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
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = val

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
            return
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
