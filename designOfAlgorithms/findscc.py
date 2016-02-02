#!/usr/bin/env python
"""This module calculates the SSC for a given graph.

The graph is given as an argument in a text file containing N (unknown)
elements. Each element contains two integers, the node the edge originates from
and the vertex it ends at (the tail and the head).

We output the sizes of the 5 largest SSCs in teh given graph, in
decreasing order, separated by commas.
"""

import sys
import resource


# Set rescursion limit and stack size limit
# sys.setrecursionlimit(10 ** 6)
# resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))

class Tracker(object):
    """ Keeps track of current parameters"""

    def __init__(self):
        self.current_time = 0
        self.current_source = None
        self.leader = {}
        self.finish_time = {}
        self.explored = set()

def dfs(graph_dict, node, tracker):
    """ Inner loop explores nodes in an SCC recursively.

    Graph is a dict tail: [head_list]
    """

    tracker.explored.add(node)
    tracker.leader[node] = tracker.current_source
    for head in graph_dict[node]:
        if head not in tracker.explored:
            dfs(graph_dict, head, tracker)
    tracker.current_time += 1
    tracker.finish_time[node] = tracker.current_time


def dfs_loop(graph_dict, nodes, tracker):
    """Outer loop that checks all SCCS."""

    for node in nodes:
        if node not in tracker.explored:
            tracker.current_source = node
            dfs(graph_dict, node, tracker)

def findSSC(data, reverse_data):
    """Implement the Kosaraju algorithm."""

    # Setup the run index for the first pass
    # During the first pass, we go from N to 1
    tracker1 = Tracker()
    tracker2 = Tracker()
    nodes = set()

    # Get the set of nodes to run on
    for tail, head_list in data.items():
        nodes |= set(head_list)
        nodes.add(tail)
    nodes = sorted(list(nodes), reverse=True)
    dfs_loop(reverse_data, nodes, tracker1)

    # Sort by the finishing time
    sorted_nodes = sorted(tracker1.finish_time,
                          key=tracker1.finish_time.get, reverse=True)
    dfs_loop(data, sorted_nodes, tracker2)
    print(parseGroups(tracker2.leader))

def parseGroups(leaderDict):
    """Takes the leader output and uses that to find groups.

    Returns the number of items in each group in descending order
    """
    leader = [value for value in leaderDict.values()]
    output = {}
    for val in leader:
        if val not in output:
            output[val] = 1
        else:
            output[val] += 1
    sizes = []
    for value in output.values():
        sizes.append(value)
    sizes.sort()
    sizes.reverse()

    return sizes


def readedgefile(inname):
    """Read the input file.

    Given the file fileName with a list of tails and heads of a directed
    Graph, Form a dictionary with each key being the tail of edges and
    the entry being an array of tails.
    """
    edge_dict = {}
    dict_reverse = {}

    finput = open(inname, 'r')
    for line in finput.readlines():
        tail, head = map(int, line.strip().split())
        if tail not in edge_dict:
            edge_dict[tail] = []
        if tail not in dict_reverse:
            dict_reverse[tail] = []
        if head not in edge_dict:
            edge_dict[head] = []
        if head not in dict_reverse:
            dict_reverse[head] = []
        dict_reverse[head].append(tail)
        edge_dict[tail].append(head)

    return edge_dict, dict_reverse


def main(argv):
    """Process Data file, then run SSC Finder."""
    filename = argv[1]
    print("Reading in File")
    data, data_rev = readedgefile(filename)
    print("Beginning Search")

    findSSC(data, data_rev)


if __name__ == "__main__":

    main(sys.argv)
