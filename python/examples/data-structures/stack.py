# __init__: Initializes the stack with an empty list.
# push(item): Adds an item to the top of the stack.
# pop(): Removes and returns the item from the top of the stack.
# peek(): Returns the item at the top of the stack without removing it.
# size(): Returns the number of items in the stack.
# is_empty(): Returns True if the stack is empty, False otherwise.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")
            return None

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0


# Example usage:
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print("Stack size:", s.size())  # Output: 3
    print("Pop:", s.pop())  # Output: 3
    print("Stack size after pop:", s.size())  # Output: 2
    print("Peek:", s.peek())  # Output: 2
