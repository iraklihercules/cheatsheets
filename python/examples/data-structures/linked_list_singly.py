# Node class: Represents each element in the linked list. Each node has two attributes:
# data, which stores the value of the node, and next, which points to the next node in the sequence.
# LinkedList class: Contains the main operations of the linked list: append, prepend, delete_node, and display.
# append(data): Adds a new node with the given data at the end of the linked list.
# prepend(data): Adds a new node with the given data at the beginning of the linked list.
# delete_node(key): Deletes the first occurrence of a node with the given data.
# display(): Prints the elements of the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
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

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        current_node = self.head

        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev.next = current_node.next
        current_node = None

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


# Example usage:
if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.prepend(0)
    linked_list.display()  # Output: 0 -> 1 -> 2 -> 3 -> None
    linked_list.delete_node(2)
    linked_list.display()  # Output: 0 -> 1 -> 3 -> None
