#!/usr/bin/python3
"""write to file"""


def write_file(filename="", text=""):
    """wrte_file using with and utf8"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        f.close()
    with open(filename, 'r', encoding="utf-8") as f:
        file = f.read()
        return sum(1 for c in file)
