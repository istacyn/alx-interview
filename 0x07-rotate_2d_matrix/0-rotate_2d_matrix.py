#!/usr/bin/python3
'''Function to rotate 2D matrix
'''


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in place.

    Args:
    - matrix: List[List[int]] - The input 2D matrix to be rotated

    Returns:
    - None
    """

    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
