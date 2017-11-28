#!/usr/bin/python3
"""fetch status"""
import urllib.request as http


with http.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    print("    - type: {}".format(type(html)))
    print("    - content: {}".format(html))
    print("    - utf8 content: {}".format(html.decode()))
