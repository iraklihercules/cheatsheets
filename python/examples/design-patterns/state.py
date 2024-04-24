# The State Pattern is a behavioral design pattern that allows an object to alter its behavior when its
# internal state changes. It encapsulates states into separate classes and delegates state-specific behavior
# to these classes, making it easier to add new states and transitions between states without changing the context class.

# - State: Defines the interface for encapsulating state-specific behavior.
# - Concrete states (StateA and StateB): Implement the State interface and define specific behavior for each state.
# They may also handle transitions to other states.
# - Context: Maintains a reference to the current state and delegates state-specific behavior to the current state object.
# - Client code: Creates an instance of the Context class and triggers requests. The context object delegates the
# handling of each request to its current state object. As the state changes, the behavior of the context object
# changes accordingly.

# In this example, the State Pattern allows the Context class to alter its behavior dynamically as its internal
# state changes. State-specific behavior is encapsulated in separate state classes, making it easier to manage
# and extend the system with new states and transitions.

# State interface
class State:
    def handle(self):
        pass


# Concrete states
class StateA(State):
    def handle(self):
        print("State A: Handling operation")
        # Transition to StateB
        return StateB()


class StateB(State):
    def handle(self):
        print("State B: Handling operation")
        # Transition to StateA
        return StateA()


# Context
class Context:
    def __init__(self):
        self._state = StateA()

    def request(self):
        self._state = self._state.handle()


# Client code
if __name__ == "__main__":
    context = Context()

    context.request()  # Output: State A: Handling operation
    context.request()  # Output: State B: Handling operation
    context.request()  # Output: State A: Handling operation
