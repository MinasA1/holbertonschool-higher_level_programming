#!/usr/bin/python3
"""fetch status"""
from requests import get


html = get('https://intranet.hbtn.io/status').content.decode('utf-8')
print("Body response:")
print("\t- type: {}".format(type(html)))
print("\t- content: {}".format(html))
