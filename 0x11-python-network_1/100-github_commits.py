#!/usr/bin/python3
"""fetch status"""
from requests import get, auth
from sys import argv


url = 'https://api.github.com/repos'
if len(argv) < 3:
    print("Usage: ./10-my_github.py <username> <password")
else:
    furl = "{}/{}/{}/commits".format(url, argv[1], argv[2])
    r = get(furl)
    js = r.json()
    for i in range(10):
        print("{}: {}".format(js[i]['parents'][0]['sha'],
                              js[i]['commit']['author']['name']))
