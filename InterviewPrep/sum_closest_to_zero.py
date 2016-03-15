"""

Given an array of numbers, return the the sum of two cloests to
0.

"""
import math

def sum_closest_to_zero(list):

    closest = abs(list[0]+list[1])

    for i in range(len(list)):
        for j in range(i+1, len(list)):
            thisval = abs(list[i]+list[j])
            if thisval < closest:
                closest = thisval

    print(closest)

input = [10,20,30]
sum_closest_to_zero(input)
input = [-5, -15, 5]
sum_closest_to_zero(input)
