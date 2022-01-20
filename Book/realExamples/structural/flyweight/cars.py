import json
from typing import Dict, List


class Flyweight:
    def __init__(self, *, shared_state: List) -> None:
        self._shared_state = shared_state

    def operation(self, *, unique_state: List) -> None:
        shared = json.dumps(self._shared_state)
        unique = json.dumps(unique_state)
        print(
            f"Flyweight: Displaying shared ({shared}) and unique ({unique}) states.",
            end="",
        )


class FlyweightFactory:
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, *, initial_flyweights: List) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state=state)] = Flyweight(
                shared_state=state
            )

    def get_key(self, *, state: List) -> str:
        return "_".join(sorted(state))

    def get_flyweight(self, *, shared_state: List) -> Flyweight:
        key = self.get_key(state=shared_state)
        if not self._flyweights.get(key):
            print(
                "FlyweightFactory: Cannot find a flyweight, creating a new one."
            )
            self._flyweights[key] = Flyweight(shared_state=shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight")
        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def add_car_to_police_database(
    factory: FlyweightFactory, car_specifications: Dict
) -> None:
    print("\n\nClient: Adding a car to database.")
    flyweight = factory.get_flyweight(
        shared_state=[
            car_specifications["brand"],
            car_specifications["model"],
            car_specifications["color"],
        ]
    )
    flyweight.operation(
        unique_state=[
            car_specifications["plates"],
            car_specifications["owner"],
        ]
    )


if __name__ == "__main__":
    factory = FlyweightFactory(
        initial_flyweights=[
            ["Chevrolet", "Camaro2018", "pink"],
            ["Mercedes Benz", "C300", "black"],
            ["Mercedes Benz", "C500", "red"],
            ["BMW", "M5", "red"],
            ["BMW", "X6", "white"],
        ]
    )
    factory.list_flyweights()
    add_car_to_police_database(
        factory=factory,
        car_specifications={
            "plates": "CL234IR",
            "owner": "James Doe",
            "brand": "BMW",
            "model": "M5",
            "color": "red",
        },
    )
    add_car_to_police_database(
        factory=factory,
        car_specifications={
            "plates": "CL234IR",
            "owner": "James Doe",
            "brand": "BMW",
            "model": "X1",
            "color": "red",
        },
    )
    print("\n")
    factory.list_flyweights()
