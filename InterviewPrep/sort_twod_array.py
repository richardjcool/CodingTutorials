"""

Given a 2d matrix of integers,  sort it such that

* every row is sorted in ascending order
* every column is sorted in ascending order from top to bottom
* all items in the same row are unique

"""


def sort_matrix(grid):

    values = []
    for row in grid[:]:
        values.extend([x for x in row])
    values.sort()

    nrow = len(grid)
    ncol = len(grid[0])

    for irow in range(nrow):
        for icol in range(ncol):
            grid[irow][icol] = values[irow*ncol+icol]

    print(grid)


grid = [[1,3,5],
        [3,2,3]]

sort_matrix(grid)
