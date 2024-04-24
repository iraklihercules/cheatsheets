# The Prototype Pattern is a creational design pattern that allows you to create new objects by copying an
# existing object, known as a prototype, instead of creating new instances from scratch. This pattern is useful
# when the construction of a new object is more efficient by copying an existing object rather than creating it
# from scratch, especially if the object creation process is complex or resource-intensive.

# Prototype: This class acts as a prototype manager that holds a collection of prototype objects and allows
# clients to register, unregister, and clone these objects.
# register_object(): Method to register a prototype object with a given name.
# unregister_object(): Method to unregister a prototype object by its name.
# clone(): Method to clone a prototype object by its name and optionally update its attributes.
# Car: This class represents a prototype object that the client wants to clone. In this example, Car instances
# represent different car models.
# Client code: In the client code, a Prototype instance is created, and a Car object is registered with the
# prototype manager. Then, the client clones the registered car object, optionally updating its year attribute,
# and prints the cloned car object.

# The Prototype Pattern allows you to create new objects by copying existing objects, providing a flexible and
# efficient way to create objects with the same structure but potentially different states. It is especially
# useful when the construction of new objects is complex or resource-intensive, as it avoids the need to
# recreate the object from scratch.

import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attrs):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attrs)
        return obj


class Car:
    def __init__(self):
        self.make = "Toyota"
        self.model = "Corolla"
        self.year = 2022

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


# Client code
if __name__ == "__main__":
    prototype = Prototype()

    car = Car()
    prototype.register_object("car", car)

    cloned_car = prototype.clone("car", year=2023)
    print(cloned_car)  # Output: 2023 Toyota Corolla

