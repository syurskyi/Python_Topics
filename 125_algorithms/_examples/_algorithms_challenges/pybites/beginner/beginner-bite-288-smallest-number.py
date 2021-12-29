"""
Write a function that accepts a list of digits and returns the smallest number that
can be created by combining unique digits.

Therefore, you have to ignore duplicated digits.

Examples:

[1] => 1

[7, 1] => 17

[1, 9, 5, 9, 1] => 159

Note: An empty input list [] should return 0.
"""

from typing import List

# Mialem jeszcze innego pomysla, zeby uzyc joina:
# s = ('').join(lista)
# jak zamienic liste intow na liste str?
# d = [str(x) for x in c]
def minimum_number(digits: List[int]) -> int:
    if len(digits) == 0:
        return 0
    reduced = set(digits)
    sort = sorted(reduced)
    r = ""
    for e in sort:
        r += str(e)
    return int(r)


print(minimum_number([1,9,5,9,1]))