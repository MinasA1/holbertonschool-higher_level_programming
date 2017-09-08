#!/usr/bin/python3
"""append to file"""


def append_write(filename="", text=""):
    """append or create file"""
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
        f.close()
    with open(filename, 'r', encoding="utf-8") as f:
        file = f.read()
        return sum(1 for c in file)
