from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, *, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, *, request: Any) -> Optional[str]:
        pass


class AbstractHandler(Handler):

    _next_handler: Optional[Handler]

    def set_next(self, *, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, *, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request=request)
        return None


class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey: I´ll eat the {request}"
        return super().handle(request=request)


class SquirreHandler(AbstractHandler):
    def handle(self, *, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I´ll eat the {request}"
        return super().handle(request=request)


class DogHandler(AbstractHandler):
    def handle(self, *, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I´ll eat the {request}"
        return super().handle(request=request)


def client_code(*, handler: Handler) -> None:
    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\nClient: who wants a {food}?")
        result = handler.handle(request=food)
        if result:
            print(f"  {result}")
        else:
            print(f"  {food} was left untouched.")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirreHandler()
    dog = DogHandler()
    monkey.set_next(handler=squirrel).set_next(handler=dog)

    print("*** Chain: Monkey > Squirrel > Dog ***")
    client_code(handler=monkey)
    print("\n")

    print("*** Subchan: Squirrel > Dog ***")
    client_code(handler=squirrel)
