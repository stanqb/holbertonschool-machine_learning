#!/usr/bin/env python3
"""Module for calculating matrix shape."""


def matrix_shape(matrix):
    """
    Calculates the shape of a matrix.

    Args:
        matrix: A nested list representing a matrix of any dimension.

    Returns:
        A list of integers representing the shape of the matrix.
    """
    shape = []
    current = matrix

    while isinstance(current, list):
        shape.append(len(current))
        if len(current) > 0:
            current = current[0]
        else:
            break

    return shape
