#!/usr/bin/python3
"""fetch status"""
import urllib.request as http
from sys import argv


if len(argv) == 1:
    print("Usage ./1-hbtn_header <URL>")
else:
    url = argv[1]
    with http.urlopen(url) as response:
        html = response.getheader('X-Request-Id')
        print(html)
