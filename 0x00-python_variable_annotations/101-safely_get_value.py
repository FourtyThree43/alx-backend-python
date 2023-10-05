#!/usr/bin/env python3
""" Module for type-annotated function safely_get_value """
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Get value from dictionary safely"""
    if key in dct:
        return dct[key]
    else:
        return default
