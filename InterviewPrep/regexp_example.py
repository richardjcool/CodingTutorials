"""
You are given a vector of strings. They have some encoded information
regarding the location of a hostage. You know that each location in
enchoded message starts with _123 and ends with _dad. You want to find
all such unique encoded locations in the text.
"""
import re

def decode(s):
    pattern = re.compile("_123(.+?)_dad")
    result = pattern.findall(s)
    if result is not None:
        for item in result:
            print(item)

if __name__ == "__main__":

    decode("_123HELP_dadIcan't breath here. They are hiding " + \
           "me in _123basement_dad")
