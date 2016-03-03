""" Brute force attempt to solve travelling salesman. """
from itertools import permutations

def distance(point1, point2):
    """Return the Euclidiean distance between two points."""
    dist = ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2) ** 0.5
    return dist


def total_distance(points):
    """Return the total distance travelled crossing the points in order."""
    # Iterate from 0 to N-2 and return the distance between pairs and sum
    return sum([distance(point, points[index+1]) for
               index, point in enumerate(points[:-1])])


def travelling_salesman(points, start=None):
    """Find shortest route to visit all cities by brute force.
    Complexity is O(N!), sooooo yeah, be careful with long lists.
    """
    start = start or points[0]
    return min([perm for perm in permutations(points) if perm[0] == start],
               key=total_distance)


def travelling_salesman_approx(points, start=None):
    """This is an approximation to make things quicker where we we always
    choose to go to the nearest city.
    """
    start = start or points[0]

    must_visit = points
    path = [start]
    must_visit.remove(start)
    while must_visit:
        # Which distance is closes to the last entry (current location)
        nearest = min(must_visit, key=lambda x: distance(path[-1], x))
        path.append(nearest)
        must_visit.remove(nearest)
    return path


def main():
    points = [[0, 0], [1, 5.7], [2, 3], [3, 7],
              [0.5, 9], [3, 5], [9, 1], [10, 5]]
    print("""The minimum distance to visit all the following points: {}
starting at {} is {}.

The optimized algoritmh yields a path long {}.""".format(
        tuple(points),
        points[0],
        total_distance(travelling_salesman(points)),
        total_distance(travelling_salesman_approx(points))))

if __name__ == "__main__":
    main()
