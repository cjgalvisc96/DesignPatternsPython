from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List, Union


class AlphabeticalOrderIterator(Iterator):
    _position: int
    _reverse: bool = False

    def __init__(self, *, collection: Union[List[Any], WordsCollection], reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(collection=self._collection, reverse=False)

    def get_reverser_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(collection=self._collection, reverse=True)

    def add_item(self, item: Any) -> None:
        self._collection.append(item)


if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverser_iterator()), end="")
