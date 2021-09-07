#!/usr/bin/python3
'''
Module contains script that fetches a passed url and displays a header variable
'''
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as resp:
        print(resp.info().get('X-Request-Id'))
