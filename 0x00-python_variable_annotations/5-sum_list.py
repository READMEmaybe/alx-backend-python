#!/usr/bin/env python3
"""This module contains a function that sums all the elements in a list."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of all the elements in a list.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of all the elements in the input list.
    """
    return sum(input_list)
