# - Product interface (Animal): Defines the interface for the products to be created. In this example, it's an abstract
# class with a method speak().
# - Concrete Products (Dog and Cat): Implements the Animal interface to provide specific behavior. In this example,
# Dog and Cat are concrete classes with their implementations of the speak() method.
# - Creator interface (AnimalFactory): Defines the interface for the factory method, which will be used to create
# products. In this example, it's an abstract class with a method create_animal().
# - Concrete Creators (DogFactory and CatFactory): Implements the AnimalFactory interface to provide specific factory
# methods for creating products. In this example, DogFactory and CatFactory are concrete classes that implement the
# create_animal() method to create Dog and Cat objects, respectively.
# - Client code: Uses the factory methods provided by the concrete creators to create products. The client code does
# not need to know the specific type of product being created; it only interacts with the factory interface.

# The Factory Method pattern allows for the creation of objects without specifying the exact class of the object
# that will be created. Instead, it defers the instantiation to subclasses, which can override the factory method
# to create different types of objects. This promotes loose coupling between the client code and the created objects,
# making the code more flexible and maintainable.


from abc import ABC, abstractmethod


# Product interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


# Concrete Product 1
class Dog(Animal):
    def speak(self):
        return "Woof!"


# Concrete Product 2
class Cat(Animal):
    def speak(self):
        return "Meow!"


# Creator interface
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass


# Concrete Creator 1
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()


# Concrete Creator 2
class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()


# Client code
if __name__ == "__main__":
    dog_factory = DogFactory()
    cat_factory = CatFactory()

    dog = dog_factory.create_animal()
    cat = cat_factory.create_animal()

    print("Dog says:", dog.speak())  # Output: Dog says: Woof!
    print("Cat says:", cat.speak())  # Output: Cat says: Meow!
