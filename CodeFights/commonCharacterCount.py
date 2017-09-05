'''DESCRIPTION: 
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
'''

def commonCharacterCount(s1, s2):
    total = 0
    checked = ''

    for char in s1:
        if char in s2 and char not in checked:
            if s1.count(char) <= s2.count(char):
                total += s1.count(char)
                checked += char
            else:
                total += s2.count(char)
                checked += char
                
    return total