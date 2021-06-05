#!/usr/bin/python3
'''
Module contains a function for writing serialized data to a text file
'''
import json
to_json_string = __import__('3-to_json_string').to_json_string
write_file = __import__('1-write_file').write_file


def save_to_json_file(my_obj, filename):
    '''
    Writes serialized data to a text file
    Args:
        my_obj :The python object to serialize
        filename: The name of the file to write to
    '''
    json_str = to_json_string(my_obj)
    write_file(filename, json_str)
