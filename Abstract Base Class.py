from abc import ABCMeta , abstractmethod
from abc import ABC , abstractmethod

# class Shape(metaclass=ABCMeta):
class Shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def print_area(self):
        return self.length*self.breadth

rect1 = Rectangle()
print(rect1.print_area())