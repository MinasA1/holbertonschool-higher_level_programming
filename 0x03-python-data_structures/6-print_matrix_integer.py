#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, item in enumerate(row):
            print("{:d}".format(item), end=" " if i != len(row)-1 else "")
        print()
