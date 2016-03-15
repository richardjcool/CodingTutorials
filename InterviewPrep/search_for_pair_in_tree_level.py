"""

Given an arbitrary tree start at "root" where each node contains
(x,y) white a boolean function find(root, x, y) that returns true
if

x is equal to x for any node in tree
y is equal to y of any node in tree
both n1 and n2 are on the same level of the tree
"""
def find(tree, root, x, y, explored=None):
    explored = explored or []

    explored.append(root)
    queue = [root]

    # First check the root
    if x in [x[0] for x in queue] and \
       y in [x[1] for x in queue]:
       return True


    stopFlag = False
    while stopFlag is False:
        #Fill a new queue will all the children
        newqueue = []
        for item in queue:
            for leaf in tree:
                if leaf[0] == item:
                    newqueue.append(leaf[1])

        #Now, search this queue
        if newqueue != []:
            queue = newqueue
            if x in [x[0] for x in queue] and \
               y in [x[1] for x in queue]:
               return True
        else:
            stopFlag = True

    return False



root = (1, 120)
tree = [ [(1, 120), (5, 15)],
         [(1, 120), (30, 70)],
         [(1, 120), (80, 110)],
         [(5, 15), (35, 40)],
         [(5, 15), (45, 50)],
         [(5, 15), (55, 65)],
         [(5, 15), (90, 100)]]
print(find(tree, root, 70, 30))
