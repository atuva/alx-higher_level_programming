#!/usr/bin/python3
'''
Module contains script for making requests that also handles exceptions
'''
import urllib.request
from urllib.error import URLError
import sys

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except URLError as e:
        if hasattr(e, 'code'):
            print('Error code: {}'.format(e.code))
