"""
Expose a creation method, delegating the implementation of this method to
subclasses
"""
from abc import ABCMeta


class IPerson(metaclass=ABCMeta):

    @staticmethod
    def person_method():
        """ Interface Method """


class Student(IPerson):

    def __init__(self):
        self.name = "Basic Student Name"

    def person_method(self):
        print("I am a student")


class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic Teacher Name"

    def person_method(self):
        print("I am a teacher")


class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()

        raise Exception("Invalid Type")


if __name__ == '__main__':
    student_one = Student()
    student_one.person_method()

    teacher_one = Teacher()
    teacher_one.person_method()

    choices = ["Student", "Invalid"]
    for choice in choices:
        person = PersonFactory.build_person(choice)
        person.person_method()
