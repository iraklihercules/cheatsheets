# Node class: Represents each element in the binary tree.
# Each node has three attributes: data, left, and right, which store the value of the node, and references to
# its left and right child nodes, respectively.

# BinaryTree class: Contains the main operations of the binary tree: __init__, insert, and the
# three traversal methods: inorder_traversal, preorder_traversal, and postorder_traversal.
# insert(data): Inserts a new node with the given data into the binary tree while maintaining the binary search tree property.
# _insert_recursively(data, current_node): A helper method to recursively insert a new node into the tree.
# Traversal methods: inorder_traversal, preorder_traversal, and postorder_traversal perform inorder, preorder,
# and postorder traversals of the binary tree, respectively.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_recursively(data, self.root)

    def _insert_recursively(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursively(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursively(data, current_node.right)
        else:
            # Duplicate data, do nothing or handle as desired
            pass

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data, end=" ")


# Example usage:
if __name__ == "__main__":
    binary_tree = BinaryTree(5)
    binary_tree.insert(3)
    binary_tree.insert(7)
    binary_tree.insert(2)
    binary_tree.insert(4)
    binary_tree.insert(6)
    binary_tree.insert(8)

    print("Inorder traversal:", end=" ")
    binary_tree.inorder_traversal(binary_tree.root)  # Output: 2 3 4 5 6 7 8
    print("\nPreorder traversal:", end=" ")
    binary_tree.preorder_traversal(binary_tree.root)  # Output: 5 3 2 4 7 6 8
    print("\nPostorder traversal:", end=" ")
    binary_tree.postorder_traversal(binary_tree.root)  # Output: 2 4 3 6 8 7 5
