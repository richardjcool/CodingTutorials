"""

Given a string and a pair of swapping indices, generate the lexicographically
largest string. Swapping can be done any number of times.

Eg:)
string = 'abdc'
indices : (1, 4) (3,4)

Answer: dbca
"""
#
# def swap_letters(s, tup):
#     """Swap the ith and jth letters"""
#
#     i, j = tup[0], tup[1]
#
#     slist = list(s)
#     temp = slist[i]
#     slist[i] = slist[j]
#     slist[j] = temp
#     return "".join(slist)
#
# def find_largest_swap(s, tuplelist):
#     # Initialize
#     maxval = s  # Assume input is largest, go from there
#     prevList = [s]
#     newmax = None
#     stopFlag = False
#
#     while stopFlag is False:
#         children = []  # will hold all new leaves
#         for item in prevList:
#             for swap in tuplelist:
#                 children.append(swap_letters(item, swap))
#
#         newmax = max(children)
#         if newmax >= maxval:
#             maxval = newmax
#             prevList = children
#         else:
#             stopFlag = True
#             return maxval

"""Even better solution using DFS"""
def find_largest_swap(s, graph):
    import depth_first_search

    connected = depth_first_search.find_connected_components(graph, range(len(s)))
    print(connected)
    slist = list(s)

    for component in connected:
        sublist = sorted([slist[x] for x in component])
        for idx, compi in enumerate(component):
            slist[compi] = sublist[idx]

    return "".join(slist)


print(find_largest_swap('acxrabdz', [(0, 2), (5,7), (2,7), (1,6)]))
