from functools import wraps


def check_type(correct_type: type):
    """
    The function uses decorators to check if a wrapped function's argument
    is same as the correct type.
    :param correct_type: Type.
    :return: Decorator function's object.
    """
    def decorator(func):
        """
        The function represent a decorator to check the type of an argument of a function.
        :param func: A function's object.
        :return: The decorator's object.
        """
        @wraps(func)
        def wrapper(arg: object) -> object:
            """
            The function checks if the argument received equals to the correct type.
            if yes - a TypeError exception will be raised.
            :param arg: The argument of the wrapped function.
            :return: The return value of the argument on the function.
            """
            if type(arg) != correct_type:
                raise TypeError
            return func(arg)
        return wrapper
    return decorator


@check_type(int)
def pass_grade(grade) -> None:
    """
    The function receives a grade and prints if the result is passed or failed.
    :param grade: A test grade.
    :return: None.
    """
    print("Passed") if grade >= 55 else print("Failed")


if __name__ == "__main__":
    pass_grade(60)
    pass_grade("7")
    