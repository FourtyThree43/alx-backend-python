#!/usr/bin/env python3
""" Module to run multiple coroutines at the same time with async"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Function that returns the list of all the delays (float values).
        The list of the delays should be in ascending order without
        using sort() because of concurrency.
    """
    list_delays: List[float] = []
    list_delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(list_delays)
