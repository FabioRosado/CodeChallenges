"""
Count the frequency of letters in texts using parallel computation.

Parallelism is about doing things in parallel that can also be done
sequentially. A common example is counting the frequency of letters.
Create a function that returns the total frequency of each letter in a
list of texts and that employs parallelism.

The letters used consists of ASCII letters `a` to `z`, inclusive, and is case
insensitive.
"""
import string
def calculate(text_input):
    """
    Counts the occurrence of every letter in a list
    :parameter text_input: List
    :returns dict
    """
    alphabet = string.ascii_lowercase
    occurrence = {}
    text = "".join(filter(str.isalpha, ''.join(text_input).lower()))
    for letter in alphabet:
        if letter in text and letter not in occurrence:
            occurrence[letter] = text.count(letter)
        elif letter in text and letter in occurrence:
            occurrence[letter] += text.count(letter)
    return occurrence


