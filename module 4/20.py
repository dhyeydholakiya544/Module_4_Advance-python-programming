How to Define a Class in Python? What Is Self?

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

my_dog = Dog("Fido", 3)
my_dog.bark()  # Output: Woof!