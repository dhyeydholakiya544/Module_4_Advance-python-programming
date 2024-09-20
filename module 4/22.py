Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle?

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# Create an instance of the Circle class
circle = Circle(4)
print(circle.area())  # Output: 50.26548245743669
print(circle.perimeter())  # Output: 25.132741228718345