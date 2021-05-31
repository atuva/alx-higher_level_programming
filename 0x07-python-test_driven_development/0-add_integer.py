#!/usr/bin/python3


def add_integer(a, b=98):
    '''Functin that adds two integers
    Args:
        a (int/float): The first parameter
        b (int/float): The second parameter
    Returns:
        a + b (int): The sum of the two parameters
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))

