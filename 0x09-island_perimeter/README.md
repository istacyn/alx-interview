# Island Perimeter
This Python script includes a function to calculate the perimeter of an island represented by a grid.

## Description

The `island_perimeter` function takes a grid as input, where:
- 0 represents water
- 1 represents land

The function calculates the perimeter of the island described in the grid based on the following rules:
- Each cell in the grid is a square with a side length of 1.
- Cells are connected horizontally/vertically (not diagonally).
- The grid is rectangular, with a width and height not exceeding 100.
- The grid is completely surrounded by water.
- There is only one island (or nothing).
- The island doesn’t have "lakes" (water inside that isn’t connected to the water surrounding the island).
