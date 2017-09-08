#!/usr/bin/python3
"""read_n_lines"""

def read_lines(filename="", nb_lines=0):
    """read_n_lines using with"""
    with open(filename, 'r', encoding="utf-8") as f:
        file = f.readlines()
        l = sum(1 for line in file)
        if nb_lines == 0 or nb_lines >= l:
            for line in file:
                print (line, end="")
        else:
            for nl, line in enumerate(file):
                print(line, end="")
                if nl == nb_lines - 1:
                    break
        f.close()
