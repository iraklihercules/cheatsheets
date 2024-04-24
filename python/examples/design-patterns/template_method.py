# The Template Method Pattern is a behavioral design pattern that defines the skeleton of an algorithm in the
# superclass but lets subclasses override specific steps of the algorithm without changing its structure.
# It promotes code reuse and allows subclasses to customize certain steps of an algorithm while maintaining
# the overall algorithm structure.

# - AbstractClass: Defines the template method template_method() that contains the skeleton of the algorithm.
# It also provides base operations (base_operation1() and base_operation2()), a required operation
# (required_operation1()), and a hook method (hook()) that can be optionally overridden by subclasses.
# - ConcreteClass: Inherits from AbstractClass and provides concrete implementations for the required
# operation (required_operation1()) and the hook method (hook()). It also inherits the template method from the superclass.
# - Client code: Creates an instance of ConcreteClass and calls its template method. This triggers the
# execution of the algorithm defined in the superclass, with specific steps implemented by the subclass.

# In this example, the Template Method Pattern allows the AbstractClass to define the overall algorithm structure
# while delegating the implementation of specific steps to ConcreteClass. Subclasses can override the required
# operation and hook methods to customize the behavior of the algorithm without changing its overall structure.
# This promotes code reuse and flexibility in defining algorithms with similar structures but varying implementations.

# Abstract class with template method
class AbstractClass:
    def template_method(self):
        self.base_operation1()
        self.required_operation1()
        self.base_operation2()
        self.hook()

    def base_operation1(self):
        print("AbstractClass: Performing Base Operation 1")

    def base_operation2(self):
        print("AbstractClass: Performing Base Operation 2")

    def required_operation1(self):
        raise NotImplementedError()

    def hook(self):
        pass


# Concrete class implementing specific steps
class ConcreteClass(AbstractClass):
    def required_operation1(self):
        print("ConcreteClass: Implementing Required Operation 1")

    def hook(self):
        print("ConcreteClass: Overriding Hook Method")


# Client code
if __name__ == "__main__":
    concrete_instance = ConcreteClass()
    concrete_instance.template_method()
