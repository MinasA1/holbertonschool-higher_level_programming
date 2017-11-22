#!/usr/bin/python3
"""find peak"""


def find_peak(list_of_integers):
    """finds peak number"""
    if list_of_integers:
        def f_peak(low, high):
            """helper function to achieve real log(n)"""
            l = (low + high)//2
            if l > 0 and list_of_integers[l] < list_of_integers[l-1]:
                return f_peak(low, m)
            elif l < (low + high) and list_of_integers[l] < list_of_integers[l+1]:
                return f_peak(l, high)
            else:
                return list_of_integers[l]
        return f_peak(0, len(list_of_integers))
