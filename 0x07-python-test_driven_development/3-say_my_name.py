#!/usr/bin/python3
'''Contains a function that prints a string with first and last name
example:
    My name is <first name> <last name>
'''


def say_my_name(first_name, last_name=""):
    '''Function that prints the first and last name passed to it
    Args:
        first_name (string): The first name
        last_name (string): The last name
    '''
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print("My name is {} {}".format(first_name, last_name))
