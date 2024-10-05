#!/usr/bin/python3
"""

Pascal's Triangle

"""


def pascal_triangle(n):
    """
    Returns pascal's triangle of height n
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(n - 1):
        last_row = triangle[-1]
        last_row_len = len(last_row)
        new_row = []
        for j in range(last_row_len + 1):
            a, b = 0, 0
            if (j - 1 > -1):
                a = last_row[j - 1]
            if (j < last_row_len):
                b = last_row[j]
            new_row.append(a + b)
        triangle.append(new_row)
    return triangle
