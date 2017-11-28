#!/usr/bin/python3                                                                                                                
"""fetch status"""
from urllib import parse, request as http, error
from sys import argv


if len(argv) < 2:
    print("Usage ./3-error_code <URL>")
else:
    url = argv[1]
    try:
        with http.urlopen(url) as response:
            print(response.read().decode())
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
