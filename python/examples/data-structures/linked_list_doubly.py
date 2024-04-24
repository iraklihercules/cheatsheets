# Node class: Represents each element in the doubly linked list. Each node has three attributes:
# data, which stores the value of the node, prev, which points to the previous node, and next,
# which points to the next node.
# DoublyLinkedList class: Contains the main operations of the doubly linked list: append, prepend,
# delete_node, and two display methods (display_forward and display_backward).
# append(data): Adds a new node with the given data at the end of the linked list.
# prepend(data): Adds a new node with the given data at the beginning of the linked list.
# delete_node(key): Deletes the first occurrence of a node with the given data.
# display_forward(): Prints the elements of the linked list in forward order.
# display_backward(): Prints the elements of the linked list in backward order.

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def delete_node(self, key):
        current_node = self.head

        while current_node:
            if current_node.data == key:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                return
            current_node = current_node.next

    def display_forward(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")

    def display_backward(self):
        current_node = self.head
        while current_node and current_node.next:
            current_node = current_node.next
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.prev
        print("None")


# Example usage:
if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.prepend(0)
    linked_list.display_forward()   # Output: 0 <-> 1 <-> 2 <-> 3 <-> None
    linked_list.delete_node(2)
    linked_list.display_forward()   # Output: 0 <-> 1 <-> 3 <-> None
    linked_list.display_backward()  # Output: 3 <-> 1 <-> 0 <-> None
