"""
Given a histogram, compute how many steps are required to melt it.

In each step, a block melts if it's edge is exposed to air.

"""

def melthistogram(hist):

    count = 0
    while sum(hist) > 0:

        newhist = hist.copy()

        for ii in range(1, len(hist)-1):
            if newhist[ii] <= min(hist[ii-1], hist[ii+1]):
                newhist[ii] -= 1   # Only the top melts
            else:
                newhist[ii] = min(hist[ii-1], hist[ii+1])
            if newhist[ii] < 0:
                newhist[ii] = 0
        # The first and last entry always goes to zero
        newhist[0] = 0
        newhist[-1] = 0

        count += 1
        hist = newhist
        print(hist)

    print(count)


hist = [5, 4, 3, 6, 0, 1]
hist = [0, 1, 1, 1, 1, 0]
melthistogram(hist)
