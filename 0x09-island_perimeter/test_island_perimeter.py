#!/usr/bin/python3

""" Module for testing island_perimeter function.
"""

import unittest

island_perimeter = __import__('0-island_perimeter').island_perimeter


class TestIslandPerimeter(unittest.TestCase):
    """ Class for testing island_perimeter function.
    """

    def test_perimeter(self):
        """ Method for testing island_perimeter function."""

        # Test case 0: Empty grid
        grid = [
            []
        ]
        assert island_perimeter(grid) == 0

        # Test case 1: Single cell island
        grid1 = [
            [1]
        ]
        assert island_perimeter(grid1) == 4

        # Test case 2: Single row island
        grid2 = [
            [1, 1, 1]
        ]
        assert island_perimeter(grid2) == 8

        # Test case 3: Single column island
        grid3 = [
            [1],
            [1],
            [1]
        ]
        assert island_perimeter(grid3) == 8

        # Test case 4: Square island
        grid4 = [
            [1, 1],
            [1, 1]
        ]
        assert island_perimeter(grid4) == 8

        # Test case 5: L-shaped island
        grid5 = [
            [1, 0, 0],
            [1, 1, 1]
        ]
        assert island_perimeter(grid5) == 10

        # Test case 6: Complex shape island
        grid6 = [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
        assert island_perimeter(grid6) == 16

        # Test case 7: No island
        grid7 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        assert island_perimeter(grid7) == 0

        # Test case 8: Single cell island in a grid
        grid8 = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        assert island_perimeter(grid8) == 4

        # Test case 9: Doub cell island in a grid
        grid9 = [
            [0, 0, 0],
            [0, 1, 1],
            [0, 0, 0]
        ]
        assert island_perimeter(grid9) == 6
