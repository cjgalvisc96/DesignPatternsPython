from abc import ABC, abstractmethod
from typing import List, Union, Any


class Item(ABC):
    @abstractmethod
    def accept(self) -> Union[NotImplementedError, Any]:
        raise NotImplementedError()


class Visitor(ABC):
    @abstractmethod
    def visit(self, item: Item) -> Union[NotImplementedError, Any]:
        raise NotImplementedError()


class CartVisitor(Visitor):
    def visit(self, item: Item) -> float:
        if isinstance(item, Book):
            cost = item.get_price()
            print(f'Book  -> Genre: "{item.get_genre()}", Cost: ${item.get_price()}')
            return cost

        elif isinstance(item, Shirt):
            cost = item.get_price()
            print(f'Shirt -> Size: "{item.get_size()}", Cost: ${item.get_price()}')
            return cost


class Shirt(Item):
    def __init__(self, *, price: float, size: str) -> None:
        self.price = price
        self.size = size

    def get_price(self) -> float:
        return self.price

    def get_size(self) -> str:
        return self.size

    def accept(self, *, visitor: Visitor) -> float:
        return visitor.visit(item=self)


class Book(Item):
    def __init__(self, *, price: float, genre: str) -> None:
        self.price = price
        self.genre = genre

    def get_price(self) -> float:
        return self.price

    def get_genre(self) -> str:

        return self.genre

    def accept(self, *, visitor: Visitor) -> float:
        return visitor.visit(item=self)


def calculate_price(items: List[Union[Shirt, Book]]) -> float:
    visitor = CartVisitor()
    total = 0
    for item in items:
        total += item.accept(visitor=visitor)
    return total


if __name__ == "__main__":
    items = [
        Shirt(price=10, size="XL"),
        Shirt(price=15, size="XXL"),
        Book(price=20, genre="Fiction"),
        Book(price=100, genre="Money"),
    ]
    total = calculate_price(items=items)
    print(f"Total Cost = ${total}")
