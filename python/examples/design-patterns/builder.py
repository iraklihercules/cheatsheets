# - Pizza: Represents the product to be built. It has attributes for size, crust, and toppings.
# - PizzaBuilder: Represents the builder, which constructs the product step by step. It provides methods to set the
# size, crust, and add toppings to the pizza.
# - set_size(), set_crust(), add_topping(): Methods for setting the attributes of the pizza. Each method returns the
# builder instance to enable method chaining.
# - build(): Method that returns the constructed pizza object.
# - Client code: In the client code, a PizzaBuilder instance is created, and methods are called to set the size,
# crust, and toppings of the pizza. Finally, the build() method is called to get the constructed pizza object.

# The Builder Pattern separates the construction of a complex object from its representation, allowing the same
# construction process to create different representations. It promotes code readability and maintainability by
# providing a clear and fluent interface for building objects.

class Pizza:
    def __init__(self):
        self.size = None
        self.crust = None
        self.toppings = []

    def __str__(self):
        return f"Size: {self.size}, Crust: {self.crust}, Toppings: {', '.join(self.toppings)}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def set_crust(self, crust):
        self.pizza.crust = crust
        return self

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self

    def build(self):
        return self.pizza


# Client code
if __name__ == "__main__":
    pizza_builder = PizzaBuilder()
    pizza = pizza_builder.set_size("Large").set_crust("Thin").add_topping("Pepperoni").add_topping("Mushrooms").build()
    print(pizza)  # Output: Size: Large, Crust: Thin, Toppings: Pepperoni, Mushrooms
