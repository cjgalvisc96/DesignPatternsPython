import copy
from datetime import datetime
from abc import ABC, abstractmethod
from typing import Dict


class Prototype(ABC):
    def __init__(self, basic_stats: Dict) -> None:
        self.height = basic_stats.get("height")
        self.age = basic_stats.get("age")
        self.defense = basic_stats.get("defense")
        self.attack = basic_stats.get("attack")

    @abstractmethod
    def clone(self):
        pass

    def basic_stats(self):
        print(
            f"Height: {self.height}"
            f"\nAge: {self.age}"
            f"\nDefense: {self.defense}"
            f"\nAttack: {self.attack}"
        )


class Shopkeeper(Prototype):
    def __init__(self, basic_stats: Dict) -> None:
        super().__init__(basic_stats=basic_stats)
        self.charisma = 200

    def clone(self):
        return copy.deepcopy(self)

    def stats(self):
        super().basic_stats()
        print(f"Charisma: {self.charisma}")


class Warrior(Prototype):
    def __init__(self, basic_stats: Dict) -> None:
        super().__init__(basic_stats=basic_stats)
        self.stamina = 100

    def clone(self):
        return copy.deepcopy(self)

    def stats(self):
        super().basic_stats()
        print(f"Stamina: {self.stamina}")


class Mage(Prototype):
    def __init__(self, basic_stats: Dict) -> None:
        super().__init__(basic_stats=basic_stats)
        self.mana = 100

    def clone(self):
        return copy.deepcopy(self)

    def stats(self):
        super().basic_stats()
        print(f"Mana: {self.mana}")


if __name__ == "__main__":
    """The protoype pattern less the time clone execution
    objects
    """
    print(f"Instantiating trader guild at: {datetime.now().time()}")
    shopkeeper_basic_stats = dict(height=100, age=70, defense=30, attack=45)
    shopkeeper_template = Shopkeeper(basic_stats=shopkeeper_basic_stats)
    warrior_stats = dict(height=200, age=80, defense=50, attack=60)
    warrior_template = Warrior(basic_stats=warrior_stats)
    mage_basic_stats = dict(height=60, age=50, defense=100, attack=100)
    mage_template = Mage(basic_stats=mage_basic_stats)
    for _ in range(100):
        shopkeeper_clone = shopkeeper_template.clone()
        warrior_clone = warrior_template.clone()
        mage_clone = mage_template.clone()
    print(f"Finished instantiating population at: {datetime.now().time()}")
