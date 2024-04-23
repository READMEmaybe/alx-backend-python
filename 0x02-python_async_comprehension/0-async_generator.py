#!/usr/bin/env python3
""" async_generator module."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields random float numbers.

    Yields:
        float: A random float number.

    Raises:
        None

    Returns:
        None
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
