#!/usr/bin/python3
"""fetch status"""
from requests import get


html =  get('https://intranet.hbtn.io/status').content.decode()
print("Body response:")
print("    - type: {}".format(type(html)))
print("    - content: {}".format(html))
