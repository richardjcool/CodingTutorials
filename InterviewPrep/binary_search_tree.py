""" Generate a binary search tree in python

Operations:
    Search --  search for an element in the tree
    Insert --  add a new element to the tree
    Delete --  ** more difficult**

"""
# Define the Node class
class Node:
    def __init__(self, key):
        self.rChild = None
        self.lChild = None
        self.data = key

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, number):
        self.size = self.size + 1
        if self.root is None:
            self.root = Node(number)
        else:
            self.insertNode(self.root, number)

    def insertNode(self, node, number):

        if number > node.data:
            if node.rChild is not None:
                self.insertNode(node.rChild, number)
            else:
                node.rChild = Node(number)
        else:
            if node.lChild is not None:
                self.insertNode(node.lChild, number)
            else:
                node.lChild = Node(number)

    def printTree(self, node):
        if node is None:
            pass
        else:
            self.printTree(node.lChild)
            print(node.data)
            self.printTree(node.rChild)


def main():
    t = Tree()
    t.insert(5)
    t.insert(3)
    t.insert(7)
    t.insert(4)
    t.insert(2)
    t.insert(1)
    t.insert(6)
    t.printTree(t.root)

if __name__ == '__main__':
    main()




# # Insert a node into the tree
# def binary_insert(root, node):
#     if root is None:
#         root = node
#     else:
#         if root.data > node.data:
#             if root.lChild is None:
#                 root.lChild = node
#             else:
#                 binary_insert(root.lChild, node)
#         else:
#             if root.rChild is None:
#                 root.rChild = node
#             else:
#                 binary_insert(root.rChild, node)
#
# # Print the tree in order
# def in_order_print(root):
#     if not root:
#         return
#     in_order_print(root.lChild)
#     print(root.data)  # The smallest element will be going fully down the left
#     in_order_print(root.rChild)
#
# # Print in preorder
# def pre_order_print(root):
#     if not root:
#         return
#     print(root.data)
#     pre_order_print(root.lChild)
#     pre_order_print(root.rChild)
#
# root = Node(3)
# binary_insert(root, Node(7))
# binary_insert(root, Node(1))
# binary_insert(root, Node(5))
#
# print("In Order:")
# print(in_order_print(root))
#
# print("Pre Order:")
# print(pre_order_print(root))
