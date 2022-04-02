"""
The Millionth Fibonacci Kata
http://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/python
"""


___ fib(n
    """Calculates the nth Fibonacci number"""
    __ n >= 0:
        r.. fibiter(1, 0, 0, 1, n)
    __ n < 0:
        a, b = 0, 1
        ___ _ __ x..(0, n, -1
            a, b = b - a, a
        r.. a


___ fibiter(a, b, p, q, count
    __ count __ 0:
        r.. b
    __ count % 2 __ 0:
        r.. fibiter(a, b, p * p + q * q, q * q + 2 * p * q, count / 2)
    ____:
        r.. fibiter(b * q + a * q + a * p, b * p + a * q, p, q, count - 1)