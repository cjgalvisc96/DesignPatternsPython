def test_iterator() -> str:
    _list = [10, 100, 1000, 10000]
    iterator = iter(_list)
    try:
        while True:
            print(iterator.__next__())
    except StopIteration:
        print("Finish list iterator")


if __name__ == "__main__":
    # Iterator
    test_iterator()

    # Generator
    even_generator = (x for x in range(10) if x % 2 == 0)
    print(next(even_generator))
    print(next(even_generator))
