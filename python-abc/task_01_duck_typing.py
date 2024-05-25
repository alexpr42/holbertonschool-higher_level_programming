#!/user/bin/python3
# task_01_duck_typing.py

from abc import ABC, abstractmethod
import math

# Define class abstracta Shape
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# Define class Circle that her Shape
class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Define class Rectangle that her Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Define func shape_info
def shape_info(shape):
    # Use ducl to call methods
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
