"""
Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.

The square of the sum of the first ten natural numbers is
(1 + 2 + ... + 10)² = 55² = 3025.

The sum of the squares of the first ten natural numbers is
1² + 2² + ... + 10² = 385.

Hence the difference between the square of the sum of the first
ten natural numbers and the sum of the squares of the first ten
natural numbers is 3025 - 385 = 2640.
"""


def square_of_sum(n):
    """Square of the sum of the n natural numbers"""
    return sum(range(n + 1)) ** 2


def sum_of_squares(n):
    """Sum of the squares of the n natural numbers"""
    return sum(x*x for x in range(n + 1))


def difference(n):
    """Difference between the two sums"""
    return abs(square_of_sum(n) - sum_of_squares(n))
