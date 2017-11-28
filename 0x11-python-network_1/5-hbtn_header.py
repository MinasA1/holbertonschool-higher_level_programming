#!/usr/bin/python3
"""fetch status"""
from requests import get
from sys import argv


if len(argv) < 2:
    print("Usage ./5-hbtn_header <URL>")
else:
    url = argv[1]
    html = get(url)
    try:
        print(html.headers['X-Request-Id'])
    except KeyError:
        pass
