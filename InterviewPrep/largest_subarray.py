"""
You are given an array of variable length which contains integers -1, 0, 1.
You are also given an integer S.

Write a O(n) time program that can find the length of the largest subarry
which sums to S
"""

def find_largest_subarray_with_sum(list, s):

    minIndex = {}
    maxIndex = {}


    sum = 0
    for idx, item in enumerate(list):
        sum += item
        if sum in minIndex:
            minIndex[sum] = min(minIndex[sum], idx+1)
            maxIndex[sum] = max(maxIndex[sum], idx+1)
        else:
            minIndex[sum] = idx+1
            maxIndex[sum] = idx+1

    print(minIndex)
    print(maxIndex)

    maxlength = 0
    for key in minIndex.keys():
        if key+s in maxIndex:
            maxlength = max(maxlength, maxIndex[key+s]-minIndex[key])

    print(maxlength)


list = [0, 1, 1, 1, 0, -1, 0, 0, 0]
find_largest_subarray_with_sum(list, 1)
