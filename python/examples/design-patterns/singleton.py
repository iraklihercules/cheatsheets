# The Singleton class defines a private class variable _instance, which holds the single instance of the class.
# The __new__ method is overridden to ensure that only one instance of the class is created.
# It checks if the _instance variable is None (indicating that no instance has been created yet)
# and creates a new instance using the super().__new__(cls) call.
# Subsequent calls to create an instance of the Singleton class return the same instance stored in the _instance variable.

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


# Example usage:
if __name__ == "__main__":
    # Creating instances of the Singleton class
    singleton1 = Singleton()
    singleton2 = Singleton()

    # Checking if both instances are the same
    print("Is singleton1 the same instance as singleton2?", singleton1 is singleton2)  # Output: True
