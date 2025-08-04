#!/usr/bin/env python3
"""Module for matrix transpose operation."""


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix.

    Args:
        matrix: A 2D list representing a matrix.

    Returns:
        A new 2D list representing the transposed matrix.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for col in range(cols):
        new_row = []
        for row in range(rows):
            new_row.append(matrix[row][col])
        transpose.append(new_row)

    return transpose
