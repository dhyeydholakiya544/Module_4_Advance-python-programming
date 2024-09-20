Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle?

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Create an instance of the Rectangle class
rect = Rectangle(5, 3)
print(rect.area())  # Output: 15