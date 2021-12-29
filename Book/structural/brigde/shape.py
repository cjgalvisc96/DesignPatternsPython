from abc import ABC, abstractmethod


class ColorInterface(ABC):
    @abstractmethod
    def get_color(self):
        pass


class Red(ColorInterface):
    def get_color(self):
        print("Color Red")


class Blue(ColorInterface):
    def get_color(self):
        print("Color Blue")


class Shape(ABC):
    def __init__(self, color: ColorInterface) -> None:
        self.color = color

    @abstractmethod
    def display(self):
        pass

    def print_color(self):
        self.color.get_color()


class Circle(Shape):
    def display(self):
        print("Circle")


class Square(Shape):
    def display(self):
        print("Square")


if __name__ == "__main__":
    red = Red()
    blue = Blue()
    red_circle = Circle(color=red)
    blue_square = Square(color=blue)
    red_circle.display()
    red_circle.print_color()
    blue_square.display()
    blue_square.print_color()
