from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class State(ABC):
    @property
    def elevator(self) -> Elevator:
        return self._elevator

    @elevator.setter
    def elevator(self, elevator: Elevator) -> None:
        self._elevator = elevator

    @abstractmethod
    def push_down_button(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def push_up_button(self) -> None:
        raise NotImplementedError()


class Elevator:
    _state = Optional[State]

    def __init__(self, *, state: State) -> None:
        self.set_elevator(state=state)

    def set_elevator(self, *, state: State) -> None:
        self._state = state
        self._state.elevator = self

    def present_state(self) -> None:
        print(f"Elevator is in {type(self._state).__name__}")

    def push_down_button(self) -> None:
        self._state.push_down_button()

    def push_up_button(self) -> None:
        self._state.push_up_button()

    def push_up_and_down_buttons_at_same_time(self) -> None:
        print("Oops... you should press one button at a time")

    def no_button_pushed(self) -> None:
        print("Press any button. Up or Down")


class FirstFloor(State):
    def push_down_button(self) -> None:
        print("Already in the bottom floor")

    def push_up_button(self) -> None:
        print("Elevator moving upward one floor.")
        self.elevator.set_elevator(state=SecondFloor())


class SecondFloor(State):
    def push_down_button(self) -> None:
        print("Elevator moving down floor...")
        self.elevator.set_elevator(state=FirstFloor())

    def push_up_button(self) -> None:
        print("Already in the top floor")


if __name__ == "__main__":
    my_elevator = Elevator(state=FirstFloor())
    my_elevator.present_state()

    my_elevator.push_up_button()
    my_elevator.present_state()

    my_elevator.push_up_and_down_buttons_at_same_time()
    my_elevator.no_button_pushed()

    my_elevator.push_up_button()
    my_elevator.present_state()

    my_elevator.push_down_button()
    my_elevator.present_state()

    my_elevator.push_down_button()
    my_elevator.present_state()
