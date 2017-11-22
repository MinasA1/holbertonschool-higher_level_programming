#!/usr/bin/python3
"""find peak"""


def find_peak(list_of_integers):
    """finds peak number"""
    if not list_of_integers:
        return
    l = len(list_of_integers)
    peak = 0
    for i, j in enumerate(list_of_integers):
        if i == 1 and i < l-1:
            if list_of_integers[i+1] < list_of_integers[i] > list_of_integers[i-1]:
                return list_of_integers[i]
        elif i == 0 and l > 1:
            if list_of_integers[i+1] < list_of_integers[i]:
                return list_of_integers[i]
        elif i == l-1 and l > 1:
            if list_of_integers[i-1] < list_of_integers[i]:
                return list_of_integers[i]
        else:
            return list_of_integers[i]

