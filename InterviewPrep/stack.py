""" A basic stack implementation for Python."""


class Stack():

    def __init__(self):
        self.list = []  # Initialize our list

    def count(self):
        return len(self.list)

    def add(self, val):
        self.list = [val] + self.list

    def pop(self):
        outval = self.list[0]
        self.list = self.list[1:]
        return outval


if __name__ == "__main__":

    stack = Stack()
    stack.add(10)
    stack.add(100)
    stack.add(1)
    stack.add(10)
    stack.add('abc')
    for x in range(10):
        stack.add(x)
    

    print(stack.count())
    print(stack.pop())
    print(stack.list)
