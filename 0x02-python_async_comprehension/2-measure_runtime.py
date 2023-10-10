#!/usr/bin/env python3
""" Module 2-measure_runtime """
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure_runtime function """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = asyncio.get_event_loop().time()

    total_time = end_time - start_time

    return total_time
