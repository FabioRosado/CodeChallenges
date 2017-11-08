'''DESCRIPTION:

Given an array of strings, return another array containing all of its longest
strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"]
'''


def allLongestStrings(inputArray):
    longestString = []
    largest_len = max(map(lambda x: len(x), inputArray))
    for item in inputArray:
        if len(item) == largest_len:
            longestString.append(item)
    return longestString
