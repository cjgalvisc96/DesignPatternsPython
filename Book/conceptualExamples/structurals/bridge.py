from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    def __init__(self, *, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (
            f"Abstraction: Base operation with:\n"
            f"{self.implementation.operation_implementation()}"
        )


class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (
            f"ExtendedAbstraction: Extended operation with:\n"
            f"{self.implementation.operation_implementation()}"
        )


class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform B."


def client_code(abstration: Abstraction) -> None:
    print(abstration.operation(), end="")


if __name__ == "__main__":
    implementation = ConcreteImplementationA()
    abstration = Abstraction(implementation=implementation)
    client_code(abstration=abstration)
    print()
    implementation = ConcreteImplementationB()
    abstration = ExtendedAbstraction(implementation=implementation)
    client_code(abstration=abstration)
