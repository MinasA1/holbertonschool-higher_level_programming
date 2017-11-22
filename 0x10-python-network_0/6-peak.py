#!/usr/bin/python3
"""find peak"""


def find_peak(list_of_integers):
    """finds peak number"""
    if not list_of_integers:
        return
    s = len(list_of_integers)
    l = s//2
    if l > 0 and list_of_integers[l] < list_of_integers[l-1]:
        return find_peak(list_of_integers[:l])
    elif l < s-1 and list_of_integers[l] < list_of_integers[l+1]:
        return find_peak(list_of_integers[l:])
    else:
        return list_of_integers[l]
