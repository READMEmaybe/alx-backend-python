#!/usr/bin/env python3
"""This module contains a function that zooms in on a list."""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zooms in on the elements of a given list.

    Args:
        lst (Tuple): The input list to be zoomed in.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        List: The zoomed-in list.

    """
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
