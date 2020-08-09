"""
7 kyu: Sum of odd numbers
http://www.codewars.com/kata/sum-of-odd-numbers/train/python
"""


___ row_sum_odd_numbers(n
    start = n ** 2 - (n - 1)
    r_ sum(range(start, start + n * 2, 2))


assert row_sum_odd_numbers(1) __ 1
assert row_sum_odd_numbers(2) __ 8
assert row_sum_odd_numbers(41) __ 68921
