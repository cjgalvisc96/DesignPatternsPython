from __future__ import annotations
from abc import ABC, abstractmethod


class BaseComponent:
    def __init__(self, mediator: Optional[Mediator] = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component1 does A.")
        self.mediator.notify(sender=self, event="A")

    def do_b(self) -> None:
        print("Component1 does B.")
        self.mediator.notify(sender=self, event="B")


class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component2 does C.")
        self.mediator.notify(sender=self, event="C")

    def do_d(self) -> None:
        print("Component2 does D.")
        self.mediator.notify(sender=self, event="D")


class Mediator(ABC):
    @abstractmethod
    def notify(self, *, sender: object, event: str) -> None:
        raise NotImplementedError()


class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, *, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()


if __name__ == "__main__":
    component1 = Component1()
    component2 = Component2()
    mediator = ConcreteMediator(component1=component1, component2=component2)

    print("Client triggers operation A.")
    component1.do_a()

    print("\n", end="")

    print("Client triggers operation D.")
    component2.do_d()
