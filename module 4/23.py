Explain Inheritance in Python with an example?

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("The dog barks.")

my_dog = Dog("Fido", "Golden Retriever")
my_dog.sound()  # Output: The dog barks.

What is init? Or What Is A Constructor In Python?

In Python, __init__ is a special method that is called when an instance of a class is created. It is used to initialize the attributes of the class. 
The __init__ method is also known as a constructor.