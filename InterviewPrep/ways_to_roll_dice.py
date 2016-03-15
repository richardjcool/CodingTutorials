"""

Given n dice each with m faces, numbering from to 1 to m, find all the ways to
get sum X1.  X is the sumation of values and 3+4 should be treated like 4+3
(don't consider permutations.

"""

def dice(m, x, n):

    def _dice(m, x, n):
        if x == 0 and n == 0:
            yield curr_dice
        elif m>0:
            while x>=0 and n>=0:
                yield from _dice(m-1, x, n)
                curr_dice[m-1] += 1
                x -= m
                n -= 1
        curr_dice[m-1] = 0

    curr_dice = [0 for _ in range(m)]
    yield from _dice(m, x, n)
    return


def main():

    m = 6
    x = 7
    n = 2

    print(m, x, n)
    for a in dice(m, x, n):
        print(a)

if __name__ == "__main__":
    main()
