#!/usr/bin/env python3
""" Creating Tasks """
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio Task that calls the wait_random function
    with the given max_delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio Task object that represents
                                        the execution of wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
