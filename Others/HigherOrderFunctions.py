from typing import Union


def selection(
    *,
    _operation: str
) -> Union[int, str]:
    def _sum(
        num_one: int,
        num_two: int
    ) -> int:
        return num_one + num_two

    def multiplication(
        num_one: int,
        num_two: int
    ) -> int:
        return num_one * num_two

    if _operation == "sum":
        return _sum
    elif _operation == "multiplication":
        return multiplication
    else:
        raise Exception("Invalid operation")


def double_number(
    number: int
) -> int:
    return number * 2


if __name__ == '__main__':
    # Owner use
    operation = selection(_operation="multiplication")
    print(operation(12, 12))

    # filter use
    numbers = [2, 5, 10, 23, 50, 33]
    result_filter = filter(lambda number: number % 5 == 0, numbers)
    print(*result_filter)

    # map use
    numbers = [2, 5, 10, 23, 50, 33]
    result_map = map(double_number, numbers)
    print(*result_map)
