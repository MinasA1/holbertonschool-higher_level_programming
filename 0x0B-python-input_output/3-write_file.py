#!/usr/bin/python3
"""write to file"""


def write_file(filename="", text=""):
    """wrte_file using with and utf8"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
