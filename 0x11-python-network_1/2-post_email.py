#!/usr/bin/python3
"""fetch status"""
from urllib import parse, request as http
from sys import argv


if len(argv) < 3:
    print("Usage ./2-post+email.py <URL> <email>")
else:
    url = argv[1]
    values = {}
    values['email'] = argv[2]
    data = parse.urlencode(values)
    data = data.encode("ascii")
    req = http.Request(url, data)
    with http.urlopen(req) as response:
        print(response.read().decode())
