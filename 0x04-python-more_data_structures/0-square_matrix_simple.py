#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix

    new_matrix = []

    for row in matrix:
        new_matrix.append([colum**2 for colum in row])

    return new_matrix
