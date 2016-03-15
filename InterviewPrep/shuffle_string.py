"""Given a string, shuffle it so no two similar letters are together."""

def most_common_in_dict(dict, notthis=None):

    maxval = 0
    maxletter = ''

    for key, value in dict.items():
        if (value > maxval) & (key != notthis):
            maxval = value
            maxletter = key
    return maxletter


def shuffle_string(str):

    dict = {}

    #Count the number of each letter.
    for c in str:
        if c in dict:
            dict[c] += 1
        else :
            dict[c] = 1

    # Get the most common letter
    newletter =  most_common_in_dict(dict)
    dict[newletter] -= 1
    outstring = newletter

    while len(outstring) < len(str):
        newletter = most_common_in_dict(dict, notthis=outstring[-1])

        if newletter == '':
            return False

        dict[newletter] -= 1
        outstring += newletter

    return outstring

string = "ABCCC"
print(shuffle_string(string))
