"""
Given an array, return the difference between the count of even numbers and
the count of odd numbers. 0 will be considered an even number.

For example, solve([0,1,2,3]) = 0 because there are two even numbers and
two odd numbers. Even - Odd = 2 - 2 = 0.

Let's now add two letters to the last example:
solve([0,1,2,3,'a','b']) = 0. Again, Even - Odd = 2 - 2 = 0. Ignore letters.

The input will be an array of lowercase letters and numbers only.
"""


def solve(a):
    diff = 0
    for i in a:
        if type(i) == int:
            if i % 2 == 0:
                diff += 1
            elif i % 2 != 0:
                diff -= 1
    return diff


print(solve([0,1,2,3,'a','b']))