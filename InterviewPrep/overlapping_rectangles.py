"""
Given the x,y coordinates, the width and length of 2 rectangles,
determine if the 2 rectangles intersect.

"""

def overlapping_rec(x1, y1, w1, h1, x2, y2, w2, h2):

    x1_extreme = (x1-w1/2., x1+w1/2.)
    y1_extreme = (y1-h1/2., y1+h1/2.)

    x2_extreme = (x2-w2/2., x2+w2/2.)
    y2_extreme = (y2-h2/2., y2+h2/2.)


    if x2_extreme[0] > x1_extreme[1]:
        return False
    if x1_extreme[0] > x2_extreme[1]:
        return False

    if y2_extreme[0] > y1_extreme[1]:
        return False
    if y1_extreme[0] > y2_extreme[1]:
        return False

    return True



print(overlapping_rec(2,2,1,1,-1,-1,3,3))
