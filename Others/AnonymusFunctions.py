from typing import Callable


if __name__ == '__main__':
    power: Callable[[int], int] = lambda x: x ** 2
    print(power(3))

    revert_string: Callable[[str], str] = lambda string: string[::-1]
    print(revert_string("Plone"))

    is_even: Callable[[int], bool] = lambda x: (x % 2 == 0)
    print(is_even(2))
    print(is_even(5))
