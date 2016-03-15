"""
Given a number, print the number of combinations you can derive from the
number that give a word (A =1, B=2)

1123:
1,1,2,3
11,23
1,1,23
11,2,3
1, 12, 3

So 5
"""
import math
def possible_letters(numList):

    if len(numList) == 1:
        return [str(numList[0])]

    down = possible_letters(numList[1:])
    set = [str(numList[0]) + x for x in down]
    set.extend([str(numList[0])+','+x for x in down])

    keep = []
    for ss in set:
        vals = map(int, ss.split(','))

        if max(vals) < 27:
            keep.append(ss)
    return keep

def count_possible_letters(numList):
    return len(possible_letters(numList))

num = 1123
# Number of places:
digits = math.floor(math.log(num, 10))+1
numList = []
for idig in range(digits):
    dig =  int((num % math.pow(10, idig+1))/math.pow(10, idig))
    num -= dig*math.pow(10, idig)
    numList.append(dig)
numList.reverse()
print(count_possible_letters(numList))
