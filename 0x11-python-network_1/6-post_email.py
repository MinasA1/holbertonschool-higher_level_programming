#!/usr/bin/python3
"""fetch status"""
from requests import post
from sys import argv


if len(argv) < 3:
    print("Usage ./6-post_email <URL> <email>")
else:
    url = argv[1]
    values = {}
    values['email'] = argv[2]
    print(post(url, data=values).content.decode())
