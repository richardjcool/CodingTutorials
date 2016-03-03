"""Knapsack solver in python using dynamic programming.

We do this by finding the most valuable sequence of items that weighs no
more than than maxweight.

`items` is a list of pairs `(value, weight)` where value is a number and
weight is a non-negative number

>>> items = [(4, 12), (2, 1), (6, 4), (1, 1), (2, 2)]
>>> knapsack(items, 15)
(11, [(2, 1), (6, 4), (1, 1), (2, 2)])
"""
import sys

def knapsack(items, maxweight):
    """Create an nItems+1 x maxWeight+1 2d list to contain the running
    values which are filled by the dynamic routine.

    There are nItems+1 rows because we need to account for choosing from
    0 up to and including N possible items
    There are maxWeight+1 columns because we need to account for running
    capacities.
    """

    bestvalues = [ [0] * (maxweight+1) for
        _ in xrange(len(items)+1)]

    # Walk through the items and fill in bestvalues
    for i, (value, weight) in enumerate(items):
        # Note that when i = 0, we care about the 1st row
        for capacity in xrange(maxweight+1):
            # Check that we have room for this item
            if weight > capacity:
                # We didn't have room. This entry is the same as the previous
                # column's so just copy that over
                bestvalues[i+1][capacity] = bestvalues[i][capacity]
            else:
                # Ok, this item fits, we have two choices:
                # 1.) What is the value if we ignore this item and propogate
                #     the current value?
                check1 = bestvalues[i][capacity]

                # 2.) The previous value plus the value of this item constrained
                #     by the capacity that would be left if this item were added
                check2 = bestvalues[i][capacity-weight] + value

                # Whichever of these is highest is what we should use
                bestvalues[i+1][capacity] = max(check1, check2)

    print(bestvalues)
    # Now figure out what was actually selected
    reconstruct = []
    N = len(items)
    j = maxweight
    for i in range(N, 0, -1):
        if bestvalues[i][j] != bestvalues[i-1][j]:
            reconstruct.append(items[i-1])
            j -= items[i-1][1]

    # Reverse the reconstruct list
    reconstruct.reverse()

    return bestvalues[len(items)][maxweight], reconstruct

if __name__ == "__main__":

    filename = 'items4.dat'
    with open(filename) as f:
        lines = f.readlines()

    maxweight = int(lines[0])
    items = [map(int, line.split()) for line in lines[1:]]

    bestvalue, reconstruct = knapsack(items, maxweight)
    print("Best possible value: {0}".format(bestvalue))
    print("Items:")
    for value, weight in reconstruct:
        print("V: {0}, W: {1}".format(value, weight))
    totalweight = sum([weight for _,weight in reconstruct])
    print("Total Weight: {0}".format(totalweight))
