def fibonacci(n, knownResults=None):
    """ Generate the nth Fibonnacci number.
    You could speed this up with a dynamic programming methodology.
    """

    if knownResults is None:
        knownResults = {}

    # Check the base case
    if n == 0:
        knownResults[n] = 0
        return knownResults[n]
    if n == 1:
        knownResults[n] = 1
        return knownResults[n]

    # Check to see if the requested value is in the dictionary
    if n in knownResults:
        return knownResults[n]

    # Since it wasn't there, fill in the data
    currfib = fibonacci(n-1, knownResults=knownResults) + \
        fibonacci(n-2, knownResults=knownResults)

    knownResults[n] = currfib
    return knownResults[n]


def robotStep(i, j, N, pathcount):
    """ Count number of steps needed to cross a NxN matrix.
    """

    # Already at the end?
    if (i == N-1) & (j == N-1):
        return (pathcount + 1)

    if (i < N-1):
        pathcount = robotStep(i+1, j, N, pathcount)  # Step Down
    if (j < N-1):
        pathcount = robotStep(i, j+1, N, pathcount)  # Step Right

    return pathcount


def permutations(a, l, r):

    if l == r:
        print("".join(a))

    for i in range(l, r+1):
        a[l], a[i] = a[i], a[l]  # Swap i and first
        permutations(a, l+1, r)
        a[l], a[i] = a[i], a[l] # Swap back




def powerset(l):

    if not l: return [[]]
    # Append the powerset of the array minus first element combined
    # all subsets starting with first element
    return powerset(l[1:]) + [[l[0]] + x for x in powerset(l[1:])]

if __name__ == "__main__":
    string = 'abc'
    n = len(string)
    s = list(string)

    permutations(s, 0, n-1)
