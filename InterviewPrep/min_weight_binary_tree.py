"""
Given a series of numbers, from a binary tree, find the minimum weight binary tree.
The weight of the node is depth*value of the element + weight of the left tree
+ weight of the right tree. Weight of the root node is the weight of the tree.
Find the minimum weight binary tree out of all possible binary trees.

Idea:
Since weight is basically sum(depth*value), we want to make sure the
highest elements are on top of the tree and the smallest elements are
in the leaves.

This clearly depends on ordering (if I fed the tree in lowest to highest,
the tree will be max weight as everything will go right. We need to add
elements to the tree in reverse order)

If there are N elements in the array:

            0
        1       2
      3   4   5   6

So the childen of the i'th node are (2i+1) and (2i+2)

It also means the tree is just the inverse list of elements
"""
def compute_weight(tree, root, depth):
    if root > len(tree) -1:
        return 0

    l = compute_weight(tree, 2*root+1, depth+1)
    r = compute_weight(tree, 2*root+2, depth+1)
    return depth*tree[root] + l + r


if __name__ == "__main__":
    nums =  [1,2,3,8,10,20,43]
    nums.sort() #sort the array
    nums = nums[::-1] #reverse so that that it is sorted max->min
    print(compute_weight(nums,0,0))
