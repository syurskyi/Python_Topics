"""
Playing with digits
http://www.codewars.com/kata/playing-with-digits/train/python
"""


___ dig_pow(n, p):
    num = str(n)
    total = sum([int(num[i]) ** (p + i) for i in range(len(num))])
    return total / n __ (total % n) == 0 else -1
