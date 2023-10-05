#!/usr/bin/env python3
""" Module for element_length function """
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns list of integers representing the lengths of the elements
        in lst """
    return [(i, len(i)) for i in lst]
