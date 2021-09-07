#!/usr/bin/python3
'''
Script that list 10 commits (from the most recent to oldest) of a specified
repo
'''
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    r = requests.get(url)

    for json in r.json()[:10]:
        print('{}: {}'.format(json.get('sha'), json.get('commit').get(
              'author').get('name')))
