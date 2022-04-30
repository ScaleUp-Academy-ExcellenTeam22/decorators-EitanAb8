from functools import wraps


def surprise_decorator(func):
    """
    The function represents a decorator wrapper for a function.
    :param func: A function's object.
    :return: A wrapper function's object.
    """
    @wraps(func)
    def wrapper() -> None:
        """
        The function wraps a function and prints Surprise.
        :return: None.
        """
        print("Surprise!")
    return wrapper


@surprise_decorator
def whats_in_the_box() -> None:
    """
    The function prints a string.
    :return: None.
    """
    print("You will probably won't reach here")


if __name__ == "__main__":
    whats_in_the_box()
