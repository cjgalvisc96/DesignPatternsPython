import six
from abc import ABCMeta
from typing import Any, Final


class Icoffee(metaclass=ABCMeta):
    IVA: Final = 0.1

    def get_cost(self) -> Any:
        pass

    def get_ingredients(self) -> Any:
        pass

    def get_tax(self) -> Any:
        return self.IVA * self.get_cost()

    def print_order(self) -> None:
        print(
            f"Ingredients: {self.get_ingredients()}"
            f"\nCost: {self.get_cost()}"
            f"\nTaxes: {self.get_tax()}"
        )


class RegularCoffee(Icoffee):
    COST: Final = 1.00

    def get_cost(self) -> float:
        return self.COST

    def get_ingredients(self) -> Any:
        return "coffee"


class LatteCoffee(Icoffee):
    COST: Final = 2.00

    def get_cost(self) -> float:
        return self.COST

    def get_ingredients(self) -> Any:
        return "coffe-extra"


@six.add_metaclass(ABCMeta)
class ICoffeeDecorator(Icoffee):
    def __init__(self, *, decorated_coffee: Icoffee) -> None:
        self.decorated_coffee = decorated_coffee

    def get_cost(self) -> Any:
        return self.decorated_coffee.get_cost()

    def get_ingredients(self) -> Any:
        return self.decorated_coffee.get_ingredients()


class Sugar(ICoffeeDecorator):
    def __init__(self, *, decorated_coffee: ICoffeeDecorator) -> None:
        ICoffeeDecorator.__init__(self, decorated_coffee=decorated_coffee)

    def get_cost(self) -> Any:
        return self.decorated_coffee.get_cost()

    def get_ingredients(self) -> Any:
        return self.decorated_coffee.get_ingredients() + ", sugar"


class Milk(ICoffeeDecorator):
    def __init__(self, *, decorated_coffee: ICoffeeDecorator) -> None:
        ICoffeeDecorator.__init__(self, decorated_coffee=decorated_coffee)

    def get_cost(self) -> Any:
        return self.decorated_coffee.get_cost() + 0.25

    def get_ingredients(self) -> Any:
        return self.decorated_coffee.get_ingredients() + ", milk"


class Vanilla(ICoffeeDecorator):
    def __init__(self, *, decorated_coffee: ICoffeeDecorator) -> None:
        ICoffeeDecorator.__init__(self, decorated_coffee=decorated_coffee)

    def get_cost(self) -> Any:
        return self.decorated_coffee.get_cost() + 0.75

    def get_ingredients(self) -> Any:
        return self.decorated_coffee.get_ingredients() + ", vanilla"


if __name__ == "__main__":
    print("***** Regular Coffee *****")
    regular_coffee = RegularCoffee()
    regular_coffee.print_order()
    print("***** Add Milk *****")
    regular_coffee = Milk(decorated_coffee=regular_coffee)
    regular_coffee.print_order()
    print("***** Add Vanilla *****")
    regular_coffee = Vanilla(decorated_coffee=regular_coffee)
    regular_coffee.print_order()
    print("***** Add Sugar *****")
    regular_coffee = Sugar(decorated_coffee=regular_coffee)
    regular_coffee.print_order()
