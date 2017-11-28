#!/usr/bin/python3
"""fetch status"""
from requests import get, auth
from sys import argv


url = 'https://api.github.com/user'
if len(argv) < 3:
    print("Usage: ./10-my_github.py <username> <password")
else:
    username = argv[1]
    password = argv[2]
    r = get(url, auth=auth.HTTPBasicAuth(username, password))
    js = r.json()
    try:
        print(js['id'])
    except KeyError:
        print(None)
