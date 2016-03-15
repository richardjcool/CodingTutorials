"""Reverse the words in a sentence."""

def reverse_words(sentence):
    """Assuming sentence starts with a capitaol and ends with period."""

    # Step 1, remove the period at the end
    punctuation = sentence[-1]
    sentence = sentence[:-1]

    # Step 2, make the first character lower case
    slist = list(sentence)
    slist[0] = slist[0].lower()
    sentence = "".join(slist)

    # Step 3, split on space
    words = sentence.split()

    # Change the order of the words
    words.reverse()

    # Make a new sentence
    sentence = " ".join(words)

    # Capitalize first letter
    slist = list(sentence)
    slist[0] = slist[0].upper()
    sentence = "".join(slist)
    sentence += punctuation

    return sentence



sentence = "Go then there are other worlds than these."
print(reverse_words(sentence))
