import asyncio
import atexit
from functools import lru_cache
import timeit


@lru_cache(maxsize=128)
def fibonacci_with_cache(number: int):
    """
    Recursive function to calculate fibonacci number.
    The function is using lru_cache - a module in functools which helps
    in reducing the execution time of the function by using memorization technique.
    :param number: A positive number.
    :return: The result of fibonacci on the argument.
    """
    if number < 2:
        return number
    return fibonacci_with_cache(number - 1) + fibonacci_with_cache(number - 2)


def fibonacci_without_cache(number: int):
    """
        Recursive function to calculate fibonacci number.
        :param number: A positive number.
        :return: The result of fibonacci on the argument.
        """
    if number < 2:
        return number
    return fibonacci_without_cache(number - 1) + fibonacci_without_cache(number - 2)


def lru_cache_test():
    print("@lru_cache demonstration:")
    print("-------------------------")
    print("Overall time taken to execute without lru_cache is:",
          timeit.timeit("fibonacci_without_cache(35)", "from __main__ import fibonacci_without_cache",
                        number=1))
    print("Overall time taken to execute with lru_cache is:",
          timeit.timeit("fibonacci_with_cache(35)", "from __main__ import fibonacci_with_cache",
                        number=1))
    print("-------------------------")


@atexit.register
def goodbye() -> None:
    """
    The function is using atexit module so the function will be execute at termination.
    :return: None
    """
    print("-------------------------")
    print("All tests are done, and now exiting. Have a nice day!")
    print("-------------------------")


async def receive_data_from_client():
    """
    The function demonstrates an awaiting for a client to send a message.
    :return: A dictionary of the json file received from client.
    """
    print('start listening')
    await asyncio.sleep(3)
    print('received data from client')
    return {'data': "Hi from client"}


async def timer():
    for i in range(10):
        print(i)
        await asyncio.sleep(1)


async def asyncio_test() -> None:
    """
    The function demonstrates the asyncio module, which can make several
    functions to run simultaneous (like threads).
    :return: None
    """
    print("asyncio demonstration:")
    print("-------------------------")
    task1 = asyncio.create_task(receive_data_from_client())
    asyncio.create_task(timer())

    print(await task1)


if __name__ == "__main__":
    lru_cache_test()
    asyncio.run(asyncio_test())
