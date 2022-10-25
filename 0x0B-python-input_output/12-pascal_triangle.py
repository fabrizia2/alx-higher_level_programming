#!/usr/bin/python3
"""Intro to Pascal's Triangle func"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n."""

    """Returns a list of lists of integers representing the triangle."""

    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        pasc = triangles[-1]
        tmp = [1]
        for i in range(len(pasc) - 1):
            tmp.append(pasc[i] + pasc[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
