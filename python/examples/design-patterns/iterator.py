# The Iterator Pattern is a behavioral design pattern that provides a way to access the elements of an aggregate
# object sequentially without exposing its underlying representation. It decouples the client code from the
# internal structure of the collection, allowing traversal of the elements of the collection without knowing
# its specific implementation.

# - Iterator: Defines the interface for accessing and traversing elements of the aggregate object. It provides
# methods for checking if there are more elements (has_next()) and retrieving the next element (next()).
# - Aggregate: Defines the interface for creating an iterator object. It declares a method create_iterator() that
# returns an iterator for traversing the elements of the aggregate object.
# - ConcreteAggregate: Implements the Aggregate interface and provides a concrete implementation for creating an iterator.
# It holds the collection of elements and creates an iterator for traversing them.
# - Client code: Creates an instance of ConcreteAggregate, adds items to it, and creates an iterator for traversing
# the elements. It then iterates over the elements using the iterator and prints them.

# In this example, the Iterator Pattern allows the client code to traverse the elements of the aggregate
# object (ConcreteAggregate) without exposing its internal structure. The client interacts with the aggregate
# object through the iterator interface, which provides a uniform way to access the elements regardless of the
# specific implementation of the aggregate.

# Iterator interface
class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def has_next(self):
        return self._index < len(self._collection)

    def next(self):
        if self.has_next():
            item = self._collection[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration()


# Aggregate interface
class Aggregate:
    def create_iterator(self):
        pass


# Concrete aggregate
class ConcreteAggregate(Aggregate):
    def __init__(self):
        self._data = []

    def add_item(self, item):
        self._data.append(item)

    def create_iterator(self):
        return Iterator(self._data)


# Client code
if __name__ == "__main__":
    aggregate = ConcreteAggregate()
    aggregate.add_item("Item 1")
    aggregate.add_item("Item 2")
    aggregate.add_item("Item 3")

    iterator = aggregate.create_iterator()

    while iterator.has_next():
        print(iterator.next())
