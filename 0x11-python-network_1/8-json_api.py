#!/usr/bin/python3
"""fetch status"""
from requests import post
from sys import argv


url = 'http://0.0.0.0:5000/search_user'
values = {'q': ""}
if len(argv) >= 2:
    values['q'] = argv[1]

r = post(url, data=values)
try:
    r.raise_for_status()
    js = r.json()
    if len(js):
        print("[{}] {}".format(js['id'], js['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
