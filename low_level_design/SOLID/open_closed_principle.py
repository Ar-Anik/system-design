"""
1. Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

> We should be able to add new behavior to a system without changing the existing code.

> Open for extension means → We can add new features or behaviors.
> Closed for modification means → We shouldn't need to change the existing code to do so.
"""

class Shape:
    def __init__(self, type, width, height, radius):
        self.type = type
        self.width = width
        self.height = height
        self.radius = radius

class ShapeCalculator:
    def calculate_area(self, shape):
        if shape.type == "rectangle":
            return shape.width * shape.height
        elif shape.type == "circle":
            return 3.14 * (shape.radius ** 2)

    def calculate_perimeter(self, shape):
        if shape.type == "rectangle":
            return 2 * (shape.width + shape.height)
        elif shape.type == "circle":
            return 2 * 3.14 * shape.radius

"""
If we want to add support for a new shape, like a triangle, we would have to modify Shape and ShapCalculator class 
both. This violating the Open/Closed Principle.
So,
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a  # side 1
        self.b = b  # side 2
        self.c = c  # side 3

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2  # semi-perimeter
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def calculate_perimeter(self):
        return self.a + self.b + self.c

"""
Benefits:
    * Safe extension: New behavior can be added without changing existing tested code.
    * Reduced risk of bugs: Prevents regressions in existing features.
    * Flexible systems: Enables adding new features by plugging in new components.
    * Better code evolution: System grows without rewriting the core.
"""
