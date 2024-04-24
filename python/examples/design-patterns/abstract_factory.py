# Abstract Product interfaces (Animal and Color): Defines the interface for the families of products to be created.
# In this example, Animal and Color are abstract classes with methods speak() and fill(), respectively.

# Concrete Product classes (Dog, Cat, White, and Black): Implements the Animal and Color interfaces to provide specific behavior.

# Abstract Factory interface (AbstractFactory): Defines the interface for the abstract factory, which will
# be used to create families of products. In this example, AbstractFactory is an abstract class with methods
# create_animal() and create_color().

# Concrete Factory classes (DogFactory and CatFactory): Implements the AbstractFactory interface to provide
# specific factory methods for creating families of products. In this example, DogFactory and CatFactory are
# concrete classes that implement the create_animal() and create_color() methods to create Dog with White and
# Cat with Black objects, respectively.

# Client code: Uses the factory methods provided by the concrete factories to create families of products.
# The client code does not need to know the specific type of product being created; it only interacts with the factory interface.

# The Abstract Factory pattern provides an interface for creating families of related or dependent objects
# without specifying their concrete classes. It promotes loose coupling between the client code and the
# created objects, making the code more flexible and maintainable.

from abc import ABC, abstractmethod


# Abstract Product interfaces
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Color(ABC):
    @abstractmethod
    def fill(self):
        pass


# Concrete Product classes
class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class White(Color):
    def fill(self):
        return "White"


class Black(Color):
    def fill(self):
        return "Black"


# Abstract Factory interface
class AbstractFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

    @abstractmethod
    def create_color(self):
        pass


# Concrete Factory classes
class DogFactory(AbstractFactory):
    def create_animal(self):
        return Dog()

    def create_color(self):
        return White()


class CatFactory(AbstractFactory):
    def create_animal(self):
        return Cat()

    def create_color(self):
        return Black()


# Client code
if __name__ == "__main__":
    dog_factory = DogFactory()
    cat_factory = CatFactory()

    dog = dog_factory.create_animal()
    cat = cat_factory.create_animal()

    white = dog_factory.create_color()
    black = cat_factory.create_color()

    print("Dog says:", dog.speak())  # Output: Dog says: Woof!
    print("Cat says:", cat.speak())  # Output: Cat says: Meow!
    print("Dog's color is:", white.fill())  # Output: Dog's color is: White
    print("Cat's color is:", black.fill())  # Output: Cat's color is: Black
