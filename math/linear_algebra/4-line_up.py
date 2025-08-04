#!/usr/bin/env python3
"""Module for element-wise array addition."""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    Args:
        arr1: First array (list of ints/floats).
        arr2: Second array (list of ints/floats).

    Returns:
        A new list containing element-wise sum, or None if shapes differ.
    """
    if len(arr1) != len(arr2):
        return None

    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])

    return result
