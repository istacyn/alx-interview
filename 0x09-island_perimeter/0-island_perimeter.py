#!/usr/bin/python3
"""
Script returns perimeter of the island described in grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.
    @grid: Represents grid where 0 represents water
    and 1 represents land.

    Return - Perimeter of the island.
    """
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                perimeter += 4
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
