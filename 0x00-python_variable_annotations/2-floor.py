#!/usr/bin/env python3
"""
This module contains a function that returns the largest integer
less than or equal to a given number.
"""
import math


def floor(n: float) -> int:
    """
    Returns the largest integer less than or equal to a given number.

    Args:
        n (float): The number to be rounded down.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
