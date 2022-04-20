#!/usr/bin/python3
'''
Module contains script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
'''
import requests
import sys

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    auth = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get(url, auth=auth)
    print(r.json().get('id'))
    print(r.json())
