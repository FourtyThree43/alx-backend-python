#!/usr/bin/env python3
from typing import Any, Mapping, Union


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[Any, None] = None) -> Union[Any, None]:
    """Get value from dictionary safely"""
    if key in dct:
        return dct[key]
    else:
        return default
