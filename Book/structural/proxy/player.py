from random import randint
from typing import Final


class Player:
    def __init__(self, *, name: str) -> None:
        self.name = name
        self.price = randint(1000000, 90000000)
        self.training = False
        self.vacation = False

    def on_training(self):
        self.training = True
        return self.training

    def on_vacation(self):
        self.vacation = True
        return self.vacation

    def get_price(self):
        return self.price

    def status(self):
        return self.vacation or self.training


class Manager:
    VALID_STATUS_PLAYER: Final = ["vacation", "training"]

    def __init__(self, *, player: Player) -> None:
        self.managed_player = player
        print(f"Managing player {self.managed_player.name}")

    def send_player_on(self, *, _type: str) -> None:
        if _type not in self.VALID_STATUS_PLAYER:
            print(f"Cannot send player on: {_type}, it´s not a valid option!")
            return

        if _type == "vacation":
            print(f"Sending player: {self.managed_player.name} on Vacation!")
            self.managed_player.on_vacation()
            return

        print(f"Sending player: {self.managed_player.name} on training!")
        self.managed_player.on_training()

    def sell_player(self, *, offer: float) -> None:
        print(f"The price if the player is: {self.managed_player.get_price()}")

        if offer > self.managed_player.get_price():
            print(f"Saying goodbye to: {self.managed_player.name}")
            return

        print(f"Saying NO to offer: {offer}, as the player is more valuable!")


if __name__ == "__main__":
    football_player = Player(name="Cristiano")
    manager = Manager(player=football_player)
    manager.send_player_on(_type="Whatever!")
    manager.send_player_on(_type="vacation")
    manager.send_player_on(_type="training")
    manager.sell_player(offer=100)
    manager.sell_player(offer=100000000)
