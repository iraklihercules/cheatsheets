# __init__: Initializes the queue with an empty list.
# enqueue(item): Adds an item to the rear of the queue.
# dequeue(): Removes and returns the item from the front of the queue.
# peek(): Returns the item at the front of the queue without removing it.
# size(): Returns the number of items in the queue.
# is_empty(): Returns True if the queue is empty, False otherwise.

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty")
            return None

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0


# Example usage:
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Queue size:", q.size())  # Output: 3
    print("Dequeue:", q.dequeue())  # Output: 1
    print("Queue size after dequeue:", q.size())  # Output: 2
    print("Peek:", q.peek())  # Output: 2

