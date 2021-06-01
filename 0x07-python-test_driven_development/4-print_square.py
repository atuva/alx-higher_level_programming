#!/usr/bin/python3
'''Contains print sqaure function
The function print_squre prints a square using the '#' character
'''


def print_square(size):
    '''Prints a square using the '#' character
    args:
        size (int): The size of the square
    '''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for i in range(size):
            print('#', end='')
        print()
