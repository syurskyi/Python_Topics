"""
1. group operations as ([^C][^V][^V]...[^V]) that has in total k operations and it gets k * # of A
2. n can be written as x_1 * x_2 * ... * x_N
3. then total operations # = x_1 + x_2 + ... + x_N
4. since p * q >= p + q for integers > 1, to min the result
5. decomposite x_1 to x_N to min the sum
"""


class Solution(object
  ___ _minSteps(self, n
    """
    :type n: int
    :rtype: int
    """
    __ n __ 1:
      r_ 0
    for i in range(2, int((n + 1) ** 0.5) + 1
      __ n % i __ 0:
        r_ i + self.minSteps(n / i)
    r_ n

  ___ minSteps(self, n
    ___ factor(n
      d = 2
      w___ d * d <= n:
        w___ n % d __ 0:
          n /= d
          yield d
        d += 1
      __ n > 1:
        yield n

    r_ sum(factor(n))
