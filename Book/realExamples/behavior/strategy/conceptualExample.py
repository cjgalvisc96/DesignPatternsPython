from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_some_bussiness_logic(self) -> None:
        print(
            "Context: sorting data using the strategy (not sure how it'll do it)"
        )
        result = self._strategy.do_algorithm(data=["a", "b", "c", "d", "e"])
        print(",".join(result))


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(
        self, *, data: List[str]
    ) -> Optional[NotImplementedError]:
        raise NotImplementedError()


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, *, data: List[str]) -> List[str]:
        print("ConcreteStrategyA")
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, *, data: List[str]) -> List[str]:
        print("ConcreteStrategyB")
        return reversed(sorted(data))


if __name__ == "__main__":
    context = Context(strategy=ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_bussiness_logic()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_bussiness_logic()
    print()

    print("Client: Strategy is set to normal sorting.")
    context.strategy = ConcreteStrategyA()
    context.do_some_bussiness_logic()
    print()
