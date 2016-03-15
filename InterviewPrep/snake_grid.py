"""Imaging a game with :

1. We want the maximal path through the left to right.
2. Each grid point(i,j) has a value -1 or positive
3. We cannot go through if v=-1
4. Must go from left side to right side, can move UP, DOWN, and RIGHT, but
   not LEFT
 """
import numpy as np

def DFS(grid, i,j,path,thisSum, thispath, pathlist):

    size = [len(grid), len(grid[0])]

    if (j < 0) | (i == size[0]) | \
       (i < 0) :
       return

    if (j == size[1]) :
        thisSum.append(path)
        pathlist.append(thispath)
        return

    if grid[i][j] == -1:
        return

    temp = grid[i][j]
    grid[i][j] = -1  # Can't go back!
    thispath.append(temp)
    DFS(grid, i-1, j, path+temp, thisSum, thispath, pathlist)  # Up
    DFS(grid, i+1, j, path+temp, thisSum, thispath, pathlist)  # DOwn
    DFS(grid, i, j+1, path+temp, thisSum, thispath, pathlist)  # Right
    grid[i][j] = temp

    return

def find_max_path(grid):

    maxval = 0
    for i in range(len(grid)):
        if grid[i][0] != -1:
            thisSum = []
            thispath = []
            pathlist = []
            DFS(grid, i, 0, 0, thisSum, thispath, pathlist)
            if thisSum != []:
                maxval = max(maxval, max(thisSum)
                
    return maxval





grid =[[-1, 3, 2, 1],
    [2, -1, 2, 4],
    [2, 2, -1, 3],
    [4, 2,  1, 2]]

print(find_max_path(grid))
