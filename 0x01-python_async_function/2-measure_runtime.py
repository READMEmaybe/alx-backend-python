""" Measures the average runtime of the wait_n function. """
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average runtime of the wait_n function.

    Args:
        n (int): The number of times to call the wait_n function.
        max_delay (int):
                The maximum delay for each call to the wait_n function.

    Returns:
        float: The average runtime of the wait_n function.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    return (end - start) / n
