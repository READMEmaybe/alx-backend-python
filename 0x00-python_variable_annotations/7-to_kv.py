#!/usr/bin/env python3
"""
This module contains a function that takes a string `k` 
and a Union of int and float `v` as arguments 
and returns a tuple with the string `k` and the square of `v`.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string `k` and a Union of int and float `v` as arguments
    and returns a tuple with the string `k` and the square of `v`.

    Args:
        k (str): The string key.
        v (Union[int, float]): The value, which can be either an int or a float.

    Returns:
        Tuple[str, float]: A tuple containing the string key `k` and the square of `v`.
    """
    return (k, v**2)
