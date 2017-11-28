#!/usr/bin/python3
"""fetch status"""
from requests import get
from sys import argv


url = 'https://swapi.co/api/people/?search='
if len(argv) < 2:
    print("Usage: ./102-starwars.py <value>")
else:
    url = url + argv[1]
    r = get(url)
    try:
        js = r.json()
        print("Number of results: {}".format(js['count']))
        result = js['results']
        for i in result:
            print(i['name'])
            for j in i['films']:
                js2 = get(j).json()
                print("\t{}".format(js2['title']))
    except ValueError:
        print("Not a valid JSON")
