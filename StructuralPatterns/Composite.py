"""
It is used to group objects as a single object.
It allows you to compose objects into tree structures and
then work with these structures as if they were individual objects.
"""

from abc import ABCMeta, abstractmethod


class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        """ Implement in child class """

    @staticmethod
    def print_department():
        """ Implement in child class """


class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Accounting Department: {self.employees}")


class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Development Department: {self.employees}")


class ParentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_departments = []

    def add(self, department):
        self.sub_departments.append(department)
        self.employees += department.employees

    def print_department(self):
        print("Parent Department")
        print(f"Parent Department Base Employees: {self.base_employees}")
        for sub_department in self.sub_departments:
            sub_department.print_department()
        print(f"Total number of Employees: {self.employees}")


if __name__ == '__main__':
    department_one = Accounting(200)
    department_two = Development(170)

    parent_department = ParentDepartment(30)
    parent_department.add(department_one)
    parent_department.add(department_two)

    parent_department.print_department()
