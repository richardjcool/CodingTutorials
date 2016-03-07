""" Count number of identical chars in a given string."""

def parseword(string):
    string = string.lower()
    count = list(map(string.count, string))
    return max(count)

def countchars(string):
    dict = {}

    for c in string:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1

    return max(dict.values())

if __name__ == "__main__":

    print(countchars("coffee"))
    print(countchars("truffle shuffle"))
