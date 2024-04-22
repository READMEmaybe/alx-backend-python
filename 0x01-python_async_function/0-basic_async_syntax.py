""" Basic asynchronous syntax """
import asyncio
import random


async def wait_random(max_delay=10):
    """
    Asynchronous function that waits for a random amount of time
        and returns the delay.

    Args:
        max_delay (float): The maximum delay in seconds (default is 10).

    Returns:
        float: The delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
