"""
This pattern restricts the alteration of the object's
structure while adding new functionality to it.
The initial class remains unchanged while a decorator
class provides additional capabilities.
"""


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


if __name__ == '__main__':
    say_whee()

