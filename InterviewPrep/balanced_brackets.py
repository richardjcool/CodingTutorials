"""
Given a series of parentheis and brackets with possible pairs of (), {},
[], write a method that will return true if the series in balanced.
"""

def balanced_brackets(s):

    # Key idea is that if you have an "open", you better make sure the
    # first close you run into is that type

    openList = []

    for c in s:
        if c in ['(', '{', '[']:
            openList.append(c)
        else:
            last = openList.pop()
            if c == ')' and last != '(':
                return False
            if c == '}' and last != '{':
                return False
            if c == ']' and last != '[':
                return False

    return True

s = "([)]{}"
print(balanced_brackets(s))
