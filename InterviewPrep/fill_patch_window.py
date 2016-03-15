"""
There is a deployment window of fixed time T. There are multiple patches that need
to be deployed.  Find solutioon to deploy patches such that the maximum time
utilized.
"""
import numpy as np

def powerset(l):

    if not l: return [[]]
    # Append the powerset of the array minus first element combined
    # all subsets starting with first element
    return powerset(l[1:]) + [[l[0]] + x for x in powerset(l[1:])]

def find_patch_combos(patches, window):
    powers = np.unique(powerset(patches))

    time_used = []

    maxval = 0
    for sset in powers:
        time_used.append(sum(sset))
        if sum(sset) > maxval and sum(sset) <= window:
            maxval = sum(sset)

    for sset in powers:
        if sum(sset) == maxval:
            print(sset)






patches = [1,1,1,2,3]
patches = [1,2,3,6]
print(find_patch_combos(patches, 5))
