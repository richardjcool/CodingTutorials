""" Problem was solved as part of technical interview for Hired."""
# import numpy as np

# walt@hired.com
# write a method called max_slice -> [1, 2, -4, 56, 7] -> [56, 7]

""" This was my brute force approach."""
# def max_slice(ll):
#     """Return the continguous subset of the
#        input array ll with largest sum.
#     """
#     nList = len(ll)
#     sums = np.zeros((nList, nList))
#     maxval = None
#     maxlist = None

#     for start in range(0, nList):
#         for end in range(start, nList):
#             sums[start, end] = sum(ll[start:(end+1)])
#             maxval = maxval or sums[start, end]
#             if sums[start,end] >= maxval:
#                 maxval = sums[start,end]
#                 maxlist = ll[start:(end+1)]

#     return maxlist


def max_slice(ll):
    """Return largest continugous subset of ll with largest sum.
    """

    # Initialize the maxval and the current subarray max
    maxval = ll[0]
    runningSum = ll[0]
    maxlist = [ll[0]]

    # Keep Track of the location in the array
    start = 0
    end = 0

    # We already included the first element from initialization
    # So start at next and check each element
    for index, item in enumerate(ll[1:]):
        # This was the complicated logic that I made boiled down.
        # If adding the new item makes the previous sum smaller than that
        # item, just start a new string.  My previous issue was this was
        # centered around 0, which is why negative numbers gave me problems.
        if item < (runningSum+item):
            end += 1
            runningSum += item
        else:
            start = index+1  # Index starts at 0 at ll[1]
            end = index+1  # Index starts at 0 at ll[1]
            runningSum = item

        # Now, check to see if this is currently the global max string
        if maxval <= runningSum:
            maxlist = ll[start:(end+1)]
            maxval = runningSum

    return maxlist


#     maxval = np.amax(sums)
#     # Brute force search
#     for start in range(0, nList):
#         for end in range(start, nList):
#             if sums[start, end] == maxval:
#                     return ll[start:(end+1)]

if __name__ == "__main__":
    print(max_slice([1, 3, 5, 5]))
    print(max_slice([1, -10, 5, 5, -100]))
    print(max_slice([-4, -3, -5, -5]))
    print(max_slice([0, 0, 0, 0]))
    print(max_slice([-1, -1, -5, -1, -1000]))
    print(max_slice([1, 3, -1, 5, 5]))
