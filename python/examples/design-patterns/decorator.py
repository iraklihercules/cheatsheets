# The Decorator Pattern is a structural design pattern that allows behavior to be added to individual objects
# dynamically, without affecting the behavior of other objects from the same class. It is useful for extending
# the functionality of objects in a flexible and reusable way.

# Coffee: Defines the interface for coffee objects. In this example, it has a method cost().
# SimpleCoffee: Represents a concrete component, i.e., a simple coffee without any additives.
# CoffeeDecorator: Acts as the base decorator class. It inherits from the Coffee interface and maintains
# a reference to a Coffee object.
# Milk, Sugar, Vanilla: Concrete decorator classes. They inherit from CoffeeDecorator and add specific
# functionalities (e.g., milk, sugar, vanilla) to the coffee object by modifying its cost() method.
# Client code: Demonstrates how decorators can be added to coffee objects dynamically to extend their
# functionality. It creates a simple coffee object and then decorates it with milk, sugar, vanilla, etc.,
# to create customized coffee with different costs.

# The Decorator Pattern allows you to add new functionalities to objects dynamically without subclassing.
# It promotes code reuse, flexibility, and maintainability by allowing behaviors to be added and removed at runtime.

# Component interface
class Coffee:
    def cost(self):
        pass


# Concrete component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5


# Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()


# Concrete decorators
class Milk(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2


class Sugar(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1


class Vanilla(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 3


# Client code
if __name__ == "__main__":
    coffee = SimpleCoffee()
    print("Cost of simple coffee:", coffee.cost())  # Output: Cost of simple coffee: 5

    coffee_with_milk = Milk(coffee)
    print("Cost of coffee with milk:", coffee_with_milk.cost())  # Output: Cost of coffee with milk: 7

    coffee_with_milk_and_sugar = Sugar(coffee_with_milk)
    print("Cost of coffee with milk and sugar:", coffee_with_milk_and_sugar.cost())  # Output: Cost of coffee with milk and sugar: 8

    coffee_with_milk_sugar_and_vanilla = Vanilla(coffee_with_milk_and_sugar)
    print("Cost of coffee with milk, sugar, and vanilla:", coffee_with_milk_sugar_and_vanilla.cost())  # Output: Cost of coffee with milk, sugar, and vanilla: 11
