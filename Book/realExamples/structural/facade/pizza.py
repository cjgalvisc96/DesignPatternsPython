# Subsystem 1
class TakeOrder:
    def order(self):
        print("Getting the order.")


# Subsystem 2
class CookPizza:
    def prepare(self):
        print("Preparing the pizza...")


# Subsystem 3
class Delivery:
    def deliver(self):
        print("Delivered the pizza.")


class FacadeOperator:
    def __init__(self) -> None:
        self.ordering = TakeOrder()
        self.preparing = CookPizza()
        self.delivering = Delivery()

    def complete_order(self) -> None:
        self.ordering.order()
        self.preparing.prepare()
        self.delivering.deliver()
        print("Order completed successfully.")


if __name__ == "__main__":
    operator = FacadeOperator()
    operator.complete_order()
