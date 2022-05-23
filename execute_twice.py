import decorator


@decorator.decorator
def execute_twice_decorator(func, *args, **kwargs):
    """
    The function receives a function and its arguments and wraps its twice.
    :param func: A function.
    :param args: Non Keyword Arguments.
    :param kwargs: Keyword Arguments.
    :return: The returned values of the function's execution.
    """
    return func(*args, **kwargs), func(*args, **kwargs)


@execute_twice_decorator
def calls_count(number: int) -> None:
    """
    The function prints the number the function was called and the number given as an argument.
    :return: None.
    """
    calls_count.counter += 1
    print("The function was called:", calls_count.counter, "times, with the integer argument:", number)


calls_count.counter = 0


if __name__ == "__main__":
    calls_count(77)
