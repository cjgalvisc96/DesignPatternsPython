class PersonSingleton:
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance is None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")

        self.name = name
        self.age = age
        PersonSingleton.__instance = self


if __name__ == '__main__':
    person_one = PersonSingleton("Mike", 9)
    print(person_one)
    person_one_pivot = PersonSingleton.get_instance()
    print(person_one_pivot)
    person_two = PersonSingleton("Bob", 25)
