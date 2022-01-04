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

____ typing _______ List

# Mialem jeszcze innego pomysla, zeby uzyc joina:
# s = ('').join(lista)
# jak zamienic liste intow na liste str?
# d = [str(x) for x in c]
___ minimum_number(d..: List[int]) -> int:
    __ l..(d..) __ 0:
        r.. 0
    reduced = set(d..)
    s.. = s..(reduced)
    r = ""
    ___ e __ s..:
        r += s..(e)
    r.. int(r)


print(minimum_number([1,9,5,9,1]))