#!/usr/bin/env python
"""This module calculates the SSC for a given graph.

The graph is given as an argument in a text file containing N (unknown)
elements. Each element contains two integers, the node the edge originates from
and the vertex it ends at (the tail and the head).

We output the sizes of the 5 largest SSCs in teh given graph, in
decreasing order, separated by commas.
"""

import sys, resource
#set rescursion limit and stack size limit
sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))

def findSSC(data, reverse_data):
    """Implement the Kosaraju algorithm.

    Pseudo code:
    1. Create Grev. By design, we do that at read in currently.

    2. Run DFSLoop on Grev and populate finishing_time()
    for each vertex.

    3. Run DFSLoop on G in decreasing order of finishing_time
    """

    # Setup the run index for the first pass
    # During the first pass, we go from N to 1
    runIndex = []
    graph_size = len(data)
    for i in range(1, graph_size+1):
        runIndex.append(i)

    fp_time, fp_leader = DFSLoop(reverse_data, runIndex)

    FTindex = sorted(fp_time, key=fp_time.__getitem__, reverse=True)
    sorted(fp_time, key=fp_time.__getitem__, reverse=True)
    # For the second pass, we run in the order of the
    # finishing time on the original data
    final_finishTime, final_leader = DFSLoop(data, FTindex)

    # Now, parse group sizes
    group_sizes = parseGroups(final_leader)
    print(group_sizes)

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


def DFSLoop(graph, runIndex):
    """The looper over the elements of the graph.

    Inputs:
        graph --- dictionary with the tails and heads of directed edges in
                  graph
        runIndex --- order in which we should run through this algorith (we
                     include this to allow use to use the finishing time)
    """
    global explored, time, finish_time_dic, leader_dic, s
    explored = []
    time = 1
    finish_time_dic = {}
    leader_dic = {}
    s = 0

    # Loop through the nodes in the order that was provided.
    for i in runIndex:
        if i not in explored:
            s = i
            DFS(graph, i)
            print("Call %s" % i)

    return finish_time_dic, leader_dic


def DFS(graph, vertex):
    """ Runs (recursively) the depth-first search.

    Inputs:
        graph - N element dictionary with heads and tails
        vertex -- starting point of search
    """
    global explored, time, finish_time_dic, leader_dic, s

    explored.append(vertex)
    leader_dic[vertex-1] = s
    for w in graph[vertex]:
        if w not in explored:
            DFS(graph, w)
    time += 1
    finish_time_dic[vertex] = time


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
