#!/usr/bin/python3
"""function numberoflines"""


def number_of_lines(filename=""):
    """read_file and count lines"""
    with open(filename, 'r', encoding='utf-8') as f:
        file = f.readlines()
        return sum(1 for line in file)
