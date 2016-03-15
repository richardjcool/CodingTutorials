"""Calculate the edit distance between two strings with three possible
operations:

1. Replace
2. Insert
3. Delete

I sucked this up with Hired!
"""
def edit_distance(s1, s2):

    # Take care of some base cases
    if s1 == s2 :
        return 0  # They are the same string
    if s1 == "":
        return len(s2)  # If one is empty, have to return the whole other string
    if s2 == "":
        return len(s1)

    # Calculate the cost for a replacement
    if s1[-1] == s2[-1]:
        subcost = 0
    else:
        subcost = 1

    # Now, we do the calculation recursively
    ReplaceDist = edit_distance(s1[:-1],s2[:-1]) + subcost
    RemoveDist = edit_distance(s1, s2[:-1]) + 1
    InsertDist = edit_distance(s1[:-1], s2) + 1

    return min(ReplaceDist, RemoveDist, InsertDist)



print(edit_distance('saturday', 'sunday'))
