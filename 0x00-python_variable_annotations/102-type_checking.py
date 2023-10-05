#!/usr/bin/env python3
""" Module for storing the zoom_array function definition. """
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Returns a list with all values multiplied by a factor. """
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
