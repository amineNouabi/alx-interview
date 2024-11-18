#!/usr/bin/python3

""" Rotate 2D Matrix module
"""


def transpose_2d_matrix(matrix):
    """ Transposes 2d matrix
    """
    n = len(matrix)
    i = 0
    while i <= n // 2:
        j = i + 1
        while j < n:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            j = j + 1
        i = i + 1


def reverse_rows_2d_matrix(matrix):
    """ Reverses rows of a 2D Matrix
    """
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """ Rotate 2d matrix
    """
    transpose_2d_matrix(matrix)
    reverse_rows_2d_matrix(matrix)
