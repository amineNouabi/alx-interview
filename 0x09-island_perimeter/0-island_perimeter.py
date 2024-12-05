#!/usr/bin/python3

""" Module defining island_perimeter function.
"""


def island_perimeter(grid):
    """ Calculates island's perimeter.
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i > 0 and not grid[i - 1][j]:
                    perimeter += 1
                if i < len(grid) - 1 and not grid[i + 1][j]:
                    perimeter += 1
                if j > 0 and not grid[i][j - 1]:
                    perimeter += 1
                if j < len(grid[i]) - 1 and not grid[i][j + 1]:
                    perimeter += 1
    return perimeter
