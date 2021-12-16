from abc import ABCMeta, abstractstaticmethod
from typing import Union

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ Interface Method """

class Student(IPerson):

    def __init__(self) -> None:
        self.name = "Student name"

    def person_method(self) -> None:
        print("I am a student")

class Teacher(IPerson):

    def __init__(self) -> None:
        self.name = "Teacher name"

    def person_method(self) -> None:
        print("I am a teacher")

class PersonFactory:

    @staticmethod
    def build_person(*, person_type: str) -> Union[Student, Teacher, Exception]:
        if person_type == "student":
            return Student()
        if person_type == "teacher":
            return Teacher()

        raise Exception("Invalid Person")

if __name__ == "__main__":
    person_to_create = "student"
    person = PersonFactory.build_person(person_type=person_to_create)
    person.person_method()

