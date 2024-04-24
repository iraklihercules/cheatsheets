# The Strategy Pattern is a behavioral design pattern that defines a family of algorithms, encapsulates
# each algorithm, and makes them interchangeable. It allows the algorithm to vary independently from clients that use it.

# - SortStrategy: Defines the interface for sorting strategies. It declares a method sort() to perform sorting.
# - BubbleSortStrategy and QuickSortStrategy: Concrete implementations of the SortStrategy interface.
# Each strategy encapsulates a sorting algorithm (bubble sort and quick sort, respectively) and implements
# the sort() method accordingly.
# - Sorter: Context class that holds a reference to a SortStrategy object. It allows clients to switch
# between different sorting strategies dynamically.
# - Client code: Creates a Sorter instance and sets its initial sorting strategy. It then uses the Sorter
# object to perform sorting on the data using the current strategy.

# In this example, the Strategy Pattern allows the sorting algorithm to vary independently from the clients that use it.
# Clients can switch between different sorting strategies (bubble sort, quick sort) without modifying their code,
# simply by providing a different strategy to the Sorter object. This promotes flexibility and reusability in the codebase.


# Strategy interface
class SortStrategy:
    def sort(self, data):
        pass


# Concrete strategies
class BubbleSortStrategy(SortStrategy):
    def sort(self, data):
        print("Bubble Sort Strategy")
        return sorted(data)


class QuickSortStrategy(SortStrategy):
    def sort(self, data):
        print("Quick Sort Strategy")
        return sorted(data)


# Context
class Sorter:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy.sort(data)


# Client code
if __name__ == "__main__":
    data = [5, 2, 7, 3, 9, 1]

    bubble_sort_strategy = BubbleSortStrategy()
    sorter = Sorter(bubble_sort_strategy)
    sorted_data = sorter.sort(data)
    print("Sorted data using Bubble Sort:", sorted_data)

    quick_sort_strategy = QuickSortStrategy()
    sorter.set_strategy(quick_sort_strategy)
    sorted_data = sorter.sort(data)
    print("Sorted data using Quick Sort:", sorted_data)
