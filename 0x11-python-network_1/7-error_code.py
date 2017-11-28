#!/usr/bin/python3
"""fetch status"""
from requests import get
from sys import argv


if len(argv) < 2:
    print("Usage ./7-error_code <URL>")
else:
    url = argv[1]
    r = get(url)
    if r.status_code < 400:
        print(r.content.decode())
    else:
        print("Error code: {}".format(r.status_code))
