from abc import ABCMeta, abstractmethod, abstractstaticmethod
from typing import Union


class IDepartment(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, *, employees: int) -> None:
        pass

    @abstractstaticmethod
    def print_department() -> None:
        pass


class Accounting(IDepartment):
    def __init__(self, *, employees: int) -> None:
        self.employees = employees

    def print_department(self) -> None:
        print(f"Accounting Department: {self.employees}")


class Development(IDepartment):
    def __init__(self, *, employees: int) -> None:
        self.employees = employees

    def print_department(self) -> None:
        print(f"Development Department: {self.employees}")


class ParentDepartment(IDepartment):
    def __init__(self, *, employees: int) -> None:
        self.employees = employees
        self.base_employees = employees
        self.sub_deparments = list()

    def add_deparment(
        self, *, department: Union[Accounting, Development]
    ) -> None:
        self.sub_deparments.append(department)
        self.employees += department.employees

    def print_department(self) -> None:
        print("ParentDepartment")
        print(f"Parent Department BaseEmployees: {self.base_employees}")
        for department in self.sub_deparments:
            department.print_department()
        print(f"Total number of employees: {self.employees}")


if __name__ == "__name__":
    department_one = Accounting(employees=200)
    department_two = Development(employees=170)
    parent_department = ParentDepartment(employees=30)
    parent_department.add_deparment(department=department_one)
    parent_department.add_deparment(department=department_two)
    parent_department.print_department()
