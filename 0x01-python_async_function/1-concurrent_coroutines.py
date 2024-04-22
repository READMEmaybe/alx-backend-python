#!/usr/bin/env python3
""" Concurrent coroutines """
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for a random delay between 0 and max_delay (inclusive)
    n times, and returns a list of the resulting delay times.

    Args:
        n (int): The number of delays to wait for.
        max_delay (int): The maximum delay time.

    Returns:
        list[float]: A list of the delay times.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
