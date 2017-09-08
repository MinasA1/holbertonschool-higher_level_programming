#!/usr/bin/python3
"""function read_dile"""


def read_file(filename=""):
    """read_file using with"""
    with open(filename, 'r', encoding='utf-8') as f:
        file = f.read()
        print(file, end="")
        f.close()
