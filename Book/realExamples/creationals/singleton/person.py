from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def print_data():
        pass


class PersonSinglenton(IPerson):
    __instance = None

    @staticmethod
    def get_instance():
        if not PersonSinglenton.__instance:
            PersonSinglenton("Default Name", 0)
        return PersonSinglenton.__instance

    def __init__(self, *, name: str, age: int) -> None:
        if PersonSinglenton.__instance is not None:
            raise Exception(
                "Singlenton cannot be instantiated more than once!"
            )
        self.name = name
        self.age = age
        PersonSinglenton.__instance = self

    @staticmethod
    def print_data():
        print(
            f"Name: {PersonSinglenton.__instance.name}"
            f"\nAge: {PersonSinglenton.__instance.age}"
        )


if __name__ == "__main__":
    person = PersonSinglenton(name="Cris", age=25)
    print(person)
    person.print_data()

    person_2 = PersonSinglenton(name="Test", age=100)
