from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List, Optional


class Subject(ABC):
    @abstractmethod
    def notify(self) -> None:
        raise NotImplementedError()


class Observer(ABC):
    @abstractmethod
    def update(self, *, subject: Subject) -> None:
        raise NotImplementedError()


class ConcreteSubject(Subject):
    _state: Optional[int] = None
    _observers: List[Observer] = []

    def attach(self, *, observer: Observer) -> None:
        print("Subject: Attach an observer.")
        self._observers.append(observer)

    def detach(self, *, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifyng observers...")
        for observer in self._observers:
            observer.update(subject=self)

    def some_bussiness_logic(self) -> None:
        print("\nSubject: I´m doing something important.")
        self._state = randrange(0, 10)
        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class ConcreteObserverA(Observer):
    def update(self, *, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, *, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    subject = ConcreteSubject()
    observer_a = ConcreteObserverA()
    subject.attach(observer=observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer=observer_b)

    subject.some_bussiness_logic()
    subject.some_bussiness_logic()

    subject.detach(observer=observer_a)

    subject.some_bussiness_logic()
