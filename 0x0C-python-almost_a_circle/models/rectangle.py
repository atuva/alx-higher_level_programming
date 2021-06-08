#!/usr/bin/python3
'''
This module contains the Rectangle Class.
'''
from models.base import Base


class Rectangle(Base):
    '''
    The rectangle class
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Constrictor method for the Rectangle class
        Args:
            width (int): The width of the rectangle instance
            height (int): The height of the rectangle instance
            x:
            y:
            id (int): The id of the instance
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        Getter method for width
        Returns:
            The width of the Rectangle instance
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter method for the width
        Args:
            value (int): The value to be set as the width
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''
        Getter method for height
        Returns:
            The height of the Rectangle instance
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter method for the height
        Args:
            value (int): The value to be set as the width
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''
        Getter method for x
        Returns:
            The value of x
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Setter methos for the width
        Args:
            value (int): The value to be set as x
        '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''
        Getter method for width
        Returns:
            The value of y
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        Setter methos for the width
        Args:
            value (int): The value to be set as y
        '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
        Returns:
            The area of a Rectangle instance
        '''
        return self.__width * self.__height

    def display(self):
        '''
        Prints in stdout the Rectangle instance with the character '#'
        '''
        x = "\n" * self.__y
        y = ' ' * self.__x
        print(x, end='')
        for i in range(self.__height):
            print(y, end='')
            for j in range(self.__width):
                print('#', end='')
                if j == self.__width - 1:
                    print()

    def __str__(self):
        '''
        Returns string representation of the instance
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        '''
        Assigns an argument to each attribute
        Args:
            *args : A list of arguments
        '''
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        else:
            for arg, value in kwargs.items():
                setattr(self, arg, value)

    def to_dictionary(self):
        '''
        Returns a dictionary representation of the Rectangle instance
        '''
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
