"""
the FibonacciSequence class has two methods that are able to compute the Fibonacci Sequence.
"""
from math import sqrt


class FibonacciSequence:

    def recursive_method(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.recursive_method(n - 1) + self.recursive_method(n - 2)

    def math_method(self, n):
        return ((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))

