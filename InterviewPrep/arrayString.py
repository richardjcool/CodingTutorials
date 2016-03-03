import numpy as np
import math

def uniqueChar(s1):
    """ Solve problem.
    Implement a alg that determines if a
    string is all unique characters.
    """
    # Initialize hash
    dict = {}

    # Check each character. If we find a duplicate, return False
    # Otherwise, add to dictionary and continue
    for c in s1:
        if c in dict:
            return False
        else:
            dict[c] = 1

    # Didn't fail, so must be unique
    return True


def uniqueCharNoHash(s1):
    """Check for unique characters without using any new structures."""
    s = list(s1)

    # Sort the list
    s = sorted(s)

    # Now step through the list and check the next character
    for ii in range(len(s)-1):
        if s[ii] == s[ii+1]:
            return False

    # If we're still here, must be unique
    return True

def isAnagram(s1, s2):
    """ Determine if s1 and s2 are anagrams."""

    scompare = s2[::-1]
    if s1 == scompare:
        return True
    else:
        return False


def rotateMatrix(matrix):
    """Rotate matrix 90 degrees"""
    N = matrix.shape[0]

    for i in range(math.floor(N/2)+1):
        last = N - 1 -i  # Last element used in this layer
        for j in range(i, N-i-1):
            offset = j-i
            temp = matrix[i,j]

            matrix[i,j] = matrix[last - offset, i]
            matrix[last - offset, i] = matrix[last, last-offset]
            matrix[last, last-offset] = matrix[j, last]
            matrix[j,last] = temp

    print(matrix)

def setRowColZero(matrix):
    """ If an element is zero, set it's row and column to zero"""
    icol = []
    jcol = []

    M = matrix.shape[0]
    N = matrix.shape[1]

    for ii in range(M):
        for jj in range(N):
            if matrix[ii,jj] == 0:
                icol.append(ii)
                jcol.append(jj)

    # If we saw no zeros, just return original matrix
    if len(icol) == 0:
        return matrix

    for ii, jj in zip(icol, jcol):
        matrix[:,jj] = 0
        matrix[ii,:] = 0

    return matrix



if __name__ == '__main__':
    """Test"""
    a = np.array([[1, 2, 3], [2, 0, 4], [0, 5, 6]])
    print(a)
    print(setRowColZero(a))
