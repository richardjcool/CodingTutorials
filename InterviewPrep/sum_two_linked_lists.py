"""
Given two linked lists representing an N digit integer (with ones -> tens ->
hundreds), write a function to sum them and output linked list

"""

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class List():
    def __init__(self):
        self.root = None

    def add(self, value):

        newnode = Node(value)
        if self.root is None:
            self.root = newnode
        else:
            node = self.root
            while (node.next is not None):
                node = node.next
            node.next = newnode


    def print(self):
        node = self.root
        while (node is not None):
            print(node.val)
            node = node.next

def sumlists(list1, list2):

    outlist = List()
    node1 = list1.root
    node2 = list2.root
    carry = 0  # For 1 carrying

    while (node1 is not None and node2 is not None):
        val = (node1.val+node2.val+carry)
        carry = int(val/10)
        outlist.add(val%10)
        node1 = node1.next
        node2 = node2.next

    if node1 is not None:
        val = (node1.val+carry)
        carry = int(val/10)
        outlist.add(val%10)
    if node2 is not None:
        val = (node2.val+carry)
        carry = int(val/10)
        outlist.add(val%10)



    while (carry != 0):
        outlist.add(carry%10)
        carry = int(val/10)

    outlist.print()


list1 = List()
num = [9,7,1,6]
for x in num:
    list1.add(x)

list2 = List()
num = [5,9,2]
for x in num:
    list2.add(x)

print(6179+295)
sumlists(list1, list2)
