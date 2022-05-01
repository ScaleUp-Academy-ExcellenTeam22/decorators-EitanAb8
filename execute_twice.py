from functools import wraps


def execute_twice_decorator(func):
    """
    The function represents a decorator executing a function twice.
    :param func: A function's object.
    :return: A wrapper's object.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        The function returns a tuple of the returned values of the arguments on the function.
        :param args: Non Keyword Arguments
        :param kwargs: Keyword Arguments
        :return: The returned values of the function's execution.
        """
        return func(*args, **kwargs), func(*args, **kwargs)
    return wrapper


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
