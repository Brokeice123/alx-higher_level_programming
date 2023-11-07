#!/usr/bin/python3
"""
Prints a pascal triangle
"""


def pascal_triangle(n):
    """returns the pascal triangle"""
    triangle = []
    for i in range(n):
        triangle.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                triangle[i].append(1)
            else:
                triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
    return triangle
