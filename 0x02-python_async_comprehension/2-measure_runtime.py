#!/usr/bin/env python3
"""
This module contains a coroutine function `measure_runtime` that measures
the total runtime of executing the `async_comprehension` function four times
in parallel using `asyncio.gather`.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Coroutine will execute async_comprehension four times in parallel
        using asyncio.gather.
        Returns:
            float: The total runtime.
    """
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.time()
    return end_time - start_time
