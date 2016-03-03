""" Implement a simple knapsack algorithm.

Stealing the problem from :
http://codereview.stackexchange.com/questions/62344/functional-knapsack-problem-in-python

This implementation uses the greedy approximation. Basically, list the items
in order of decreasing order of v/w and then add them until you can no
longer add items.  If m is the max value that can fit, this approximation
will get you at least m/2.


"""
from collections import namedtuple

# Inialize an object to hold the information for each object
Item = namedtuple("Item", "name weight value".split())


# Initialize the items that are offered
ITEMS = [
    Item("map", 9, 150),
    Item("compass", 13, 35),
    Item("water", 153, 200),
    Item("sandwich", 50, 160),
    Item("glucose", 15, 60),
    Item("tin", 68, 45),
    Item("banana", 27, 60),
    Item("apple", 39, 40),
    Item("cheese", 23, 30),
    Item("beer", 52, 10),
    Item("suntan cream", 11, 70),
    Item("camera", 32, 30),
    Item("t-shirt", 24, 15),
    Item("trousers", 48, 10),
    Item("umbrella", 73, 40),
    Item("waterproof trousers", 42, 70),
    Item("waterproof overclothes", 43, 75),
    Item("note-case", 22, 80),
    Item("sunglasses", 7, 20),
    Item("towel", 18, 12),
    Item("socks", 4, 50),
    Item("book", 30, 10),
]


def efficiency(item):
    """Return the value per weight of a given item."""
    return float(item.value) / float(item.weight)


def packing(items=ITEMS, max_weight=400):
    """Return a list of items with the maximum value, subject
    to the constraint that the combined weight must not exceed
    max_weight.

    """
    def pack(item):
        # Attemp to pack an item; return True if we were able to
        if item.weight <= pack.max_weight:
            # We have room for this object, so add it, and decriment
            # the max_weight remaining
            pack.max_weight -= item.weight
            return True
        else:
            return False

    pack.max_weight = max_weight
    # The filter function will iterate over a function and
    # construct a list of elements that returned True
    return filter(pack, sorted(items, key=efficiency, reverse=True))

pack = packing()
table = zip(*pack)
print("Total Value: %i"  % sum(table[2]))
print("Total Weight: %i" % sum(table[1]))
