"""
Playing with digits
http://www.codewars.com/kata/playing-with-digits/train/python
"""


___ dig_pow(n, p):
    num = str(n)
    total = s..([int(num[i]) ** (p + i) ___ i __ r..(l..(num))])
    r.. total / n __ (total % n) __ 0 ____ -1
