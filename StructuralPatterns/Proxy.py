"""
It is used to create objects that can represent functions of other
classes or objects and the interface is used to access these functionalities
"""

from abc import ABCMeta


class IPerson(metaclass=ABCMeta):

    @staticmethod
    def person_method():
        """ Interface Method """


class Person(IPerson):
    def person_method(self):
        print("I am a person!")


class ProxyPerson(IPerson):

    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("I am the proxy functionality!")
        self.person.person_method()


if __name__ == '__main__':
    person_one = Person()
    person_one.person_method()

    person_two = ProxyPerson()
    person_two.person_method()
