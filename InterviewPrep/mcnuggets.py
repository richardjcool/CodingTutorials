"""
McDonald's sells Chicken Nuggest in packages of 6, 9, and 20. Thus
it is possible to buy 15 (6+9), but not 16. Write a function that takes
n and returns True if you can create that number with 6, 9, and 20.
False if else.
"""
import math

def nuggets(n):

    for a in range(math.floor(n/6)+1):
        for b in range(math.floor(n/9)+1):
            if (n-a*6-b*9) % 20 == 0 & (n-a*6-b*9) >= 0:
                return True
    return False

if __name__ == "__main__":

    print(math.floor(1e6/6)+1)
    print(math.floor(1e6/9)+1)
