# Node class: Represents each element in the binary tree. Each node has three attributes:
# data, which stores the value of the node, left, which points to the left child node, and right,
# which points to the right child node.

# BinaryTree class: Contains the main operations of the binary tree: __init__ (to initialize the tree
# with a root node), insert (to insert a new node into the tree), and inorder_traversal (to perform an
# inorder traversal of the tree).
# insert(data): Inserts a new node with the given data into the binary tree while maintaining the binary
# search tree property (nodes to the left are smaller, nodes to the right are larger).
# _insert_recursively(data, current_node): A helper method to recursively insert a new node into the tree.
# inorder_traversal(node): Performs an inorder traversal of the binary tree, which visits the left subtree,
# then the root, and finally the right subtree.

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


# Example usage:
if __name__ == "__main__":
    binary_tree = BinaryTree(5)
    binary_tree.insert(3)
    binary_tree.insert(7)
    binary_tree.insert(2)
    binary_tree.insert(4)
    binary_tree.insert(6)
    binary_tree.insert(8)

    # Perform an inorder traversal to print the elements in sorted order
    binary_tree.inorder_traversal(binary_tree.root)  # Output: 2 3 4 5 6 7 8
