#!/usr/bin/python3
'''
Module contains a script for sending a post request with an email
'''
import urllib.parse
import urllib.request
import sys


if __name__ == '__main__':
    email = sys.argv[2]
    url = sys.argv[1]
    values = {'email': email}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
