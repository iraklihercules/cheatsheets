# https://www.youtube.com/watch?v=6oL-0TdVy28

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if "preorder" == traversal_type:
            return self.preorder_print(self.root, [])
        if "inorder" == traversal_type:
            return self.inorder_print(self.root, [])
        if "postorder" == traversal_type:
            return self.postorder_print(self.root, [])
        return f"Traversal type {traversal_type} is not implemented!"

    def preorder_print(self, curr_node, data):
        """ Root -> Left -> Right """
        if curr_node:
            data.append(curr_node.value)
            data = self.preorder_print(curr_node.left, data)
            data = self.preorder_print(curr_node.right, data)
        return data

    def inorder_print(self, curr_node, data):
        """ Left -> Root -> Right """
        if curr_node:
            data = self.inorder_print(curr_node.left, data)
            data.append(curr_node.value)
            data = self.inorder_print(curr_node.right, data)
        return data

    def postorder_print(self, curr_node, data):
        """ Left -> Right -> Root """
        if curr_node:
            data = self.postorder_print(curr_node.left, data)
            data = self.postorder_print(curr_node.right, data)
            data.append(curr_node.value)
        return data


# [1, 2, 4, 5, 3, 6, 7] Preorder
# [4, 2, 5, 1, 6, 3, 7] Inorder
# [4, 5, 2, 6, 7, 3, 1] Postorder
#
#       1
#     _/ \_
#    2     3
#   / \   / \
#  4   5 6   7


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
