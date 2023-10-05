#!/usr/bin/env python3
""" Module that takes a list input and returns the first element """
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Function that takes a list input and returns the first element """
    if lst:
        return lst[0]
    else:
        return None
