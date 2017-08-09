#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(''.join('{:2d}'.format(item) for item in row))
