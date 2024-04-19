#!/usr/bin/env python3
"""
This module contains a function that multiplies a number by a given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a given number by the multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]:
                A function that takes a float as input
                        and returns the multiplied value.

    """

    def mult(m: float) -> float:
        """Multiplies a given number by the multiplier.

        Args:
            m (float): The number to be multiplied.

        Returns:
            float: The multiplied value.

        """
        return m * multiplier

    return mult
