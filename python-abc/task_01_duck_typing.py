#!/user/bin/python3
# task_01_duck_typing.py

from abc import ABC, abstractmethod
import math

# De class abstracta Shape
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Def class to her shape
class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius


    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Def class rectangle that her shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Def shape func
def shape_info(shape):
    # use duck to call
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

