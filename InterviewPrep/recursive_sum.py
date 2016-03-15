"""
Write a recursive function sum(x, max) that calculates the sum of numbers
from x to max (inclusive). For example, sum(4, 7) would compute 4+5+6+7
"""

def sum(x, max):

    if max == x:
        return x

    return (max + sum(x, max-1))

print(sum(4,8))
