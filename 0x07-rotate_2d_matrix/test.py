#!/usr/bin/python3

""" Rotate 2D Matrix Test Module
"""

import unittest


rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix


class TestRotate2DMatrix(unittest.TestCase):
    """ Test Rotate 2D Matrix
    """

    def test_rotate_2d_matrix(self):
        """ Test Rotate 2D Matrix
        """
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        rotate_2d_matrix(matrix)
        self.assertEqual(matrix, [[7, 4, 1],
                                  [8, 5, 2],
                                  [9, 6, 3]])

        matrix = [[1, 2],
                  [3, 4]]
        rotate_2d_matrix(matrix)
        self.assertEqual(matrix, [[3, 1],
                                  [4, 2]])

        matrix = [[1]]
        rotate_2d_matrix(matrix)
        self.assertEqual(matrix, [[1]])

        matrix = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]]

        rotate_2d_matrix(matrix)
        self.assertEqual(matrix, [[13, 9, 5, 1],
                                  [14, 10, 6, 2],
                                  [15, 11, 7, 3],
                                  [16, 12, 8, 4]])

        matrix = []
        rotate_2d_matrix(matrix)
        self.assertEqual(matrix, [])

        matrix = [[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25]]
        rotate_2d_matrix(matrix)
        self.assertEqual(matrix, [[21, 16, 11, 6, 1],
                                  [22, 17, 12, 7, 2],
                                  [23, 18, 13, 8, 3],
                                  [24, 19, 14, 9, 4],
                                  [25, 20, 15, 10, 5]])

        matrix = [[1, 2, 3, 4, 5, 6],
                  [7, 8, 9, 10, 11, 12],
                  [13, 14, 15, 16, 17, 18],
                  [19, 20, 21, 22, 23, 24],
                  [25, 26, 27, 28, 29, 30],
                  [31, 32, 33, 34, 35, 36]]
        rotate_2d_matrix(matrix)
        self.assertEqual(matrix, [[31, 25, 19, 13, 7, 1],
                                  [32, 26, 20, 14, 8, 2],
                                  [33, 27, 21, 15, 9, 3],
                                  [34, 28, 22, 16, 10, 4],
                                  [35, 29, 23, 17, 11, 5],
                                  [36, 30, 24, 18, 12, 6]])


if __name__ == '__main__':
    unittest.main()
