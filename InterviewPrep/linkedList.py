class Node:

    def __init__(self, val):
        self.data = val  # The actual values
        self.next = None   # The next element in the list

class LinkedList:

    def __init__(self):
        self.head = None  # The head of the list

    def isEmpty(self):
         return self.head is None

    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def size(self):
        current = self.head
        count = 0
        while (current is not None):
            count += 1
            current = current.next
        return count

    def search(self, val):
        current = self.head
        found = False
        while (current is not None):
            # Is it this item?
            if current.data == val:
                return True
            current = current.next  # move to next item

    def remove(self, val):
        current = self.head
        previous = None
        found = False

        while (not found) and (current is not None) :
            if current.data == val:
                found = True
            else:
                previous = current
                current = current.next

        # Only do this if we actually found the element
        if found :
            if previous is None:
                # This means that we found it in the first entry
                # So just move the head to the next item
                self.head = current.next
            else:
                # Otherwise, make the next element to our previous one
                # to the value after the current one.
                previous.next = current.next



if __name__ == "__main__":

    list = LinkedList()
    list.add(10)
    list.add(13)
    for x in range(0, 100, 23):
        list.add(x)
    list.add(130)
    list.add(1)

    print(list.size())
    print(list.search(130))
    list.remove(1)
    list.remove(-100)
    print(list.size())
