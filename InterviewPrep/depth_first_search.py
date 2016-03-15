"""Python implementation of depth first search"""
def DFS(graph, start, explored=None):
    """Return the explored area of a depth first search."""
    explored = explored or []  # If none was given, start with empty
    explored.append(start)
    for point in graph:
        if point[0] == start:
            if point[1] not in explored:
                explored = DFS(graph, point[1], explored=explored)
        if point[1] == start:
            if point[0] not in explored:
                explored = DFS(graph, point[0], explored=explored)

    return explored

def find_connected_components(graph, nodes):
    """Find the connected components that includes every node in nodes."""
    fullexplored = []
    connected = []

    for node in nodes:
        if node not in fullexplored:
            connected.append(DFS(graph, node))
            fullexplored.extend(connected)
    return connected
