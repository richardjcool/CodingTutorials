""" This is a simple implementation of a queue in python."""


class Queue():

    def __init__(self):
        self.list = []

    def enqueue(self, val):
        """ Add val to the end of the queue."""
        self.list = self.list + [val]

    def dequeue(self):
        """ Remove first item from the queue."""
        try:
            outval = self.list[0]
            self.list = self.list[1:]
            return outval
        except IndexError:
            print("You cannot dequeue an empty queue.")
            raise

    def count(self):
        """ Return the current queue length"""
        return len(self.list)


if __name__ == "__main__":

    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(None)
    for x in range(10):
        queue.enqueue(x)

    for x in range(15):
        print(queue.dequeue())
