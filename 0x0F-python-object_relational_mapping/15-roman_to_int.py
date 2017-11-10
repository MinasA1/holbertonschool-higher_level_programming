#!/usr/bin/python3
"""roman_to_int"""


def roman_to_int(roman_string):
    """roman_to_int"""
    if roman_string is None:
        return 0
    if type(roman_string) is not str:
        return 0
    map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    i = 0
    while (i < len(roman_string)):
        num1 = map[roman_string[i]]
        if i+1 < len(roman_string):
            num2 = map[roman_string[i+1]]
            if (num1 >= num2):
                num += num1
                i += 1
            else:
                num += num2 - num1
                i += 2
        else:
            num += num1
            i += 1
    return num
