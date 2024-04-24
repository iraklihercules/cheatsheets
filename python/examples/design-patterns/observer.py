# The Observer Pattern is a behavioral design pattern where an object, known as the subject,
# maintains a list of its dependents, called observers, and notifies them of any changes in state,
# usually by calling one of their methods. This pattern is commonly used in event handling systems,
# where an object (subject) needs to notify multiple other objects (observers) about changes in its state.

# - Subject: Defines the interface for attaching, detaching, and notifying observers. It maintains a list of
# observers and notifies them of changes in state.
# - Observer: Defines the interface for objects that are notified of changes in the subject's state.
# - ConcreteObserver: Implements the Observer interface and defines the behavior to be executed when notified
# of changes in the subject's state.
# - ConcreteSubject: Extends the Subject class and represents the object being observed. It maintains its state
# and notifies observers of any changes in state.
# - Client code: Creates instances of ConcreteSubject and ConcreteObserver, attaches observers to the subject,
# and changes the subject's state. When the state changes, observers are notified and perform their update actions.

# In this example, the ConcreteSubject maintains a list of observers and notifies them whenever its state
# changes using the notify method. ConcreteObserver instances are attached to the ConcreteSubject and are
# updated when notified of changes in the subject's state.

# Subject interface
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


# Observer interface
class Observer:
    def update(self, message):
        pass


# Concrete Observer
class ConcreteObserver(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, message):
        print(f"{self._name} received message: {message}")


# Concrete Subject
class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self._state = None

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state
        self.notify(state)


# Client code
if __name__ == "__main__":
    subject = ConcreteSubject()

    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")

    subject.attach(observer1)
    subject.attach(observer2)

    subject.set_state("New state!")
