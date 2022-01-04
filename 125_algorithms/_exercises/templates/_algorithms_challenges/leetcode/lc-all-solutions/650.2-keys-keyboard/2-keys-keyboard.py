"""
1. group operations as ([^C][^V][^V]...[^V]) that has in total k operations and it gets k * # of A
2. n can be written as x_1 * x_2 * ... * x_N
3. then total operations # = x_1 + x_2 + ... + x_N
4. since p * q >= p + q for integers > 1, to min the result
5. decomposite x_1 to x_N to min the sum
"""


c_ Solution(object):
  ___ _minSteps(self, n):
    """
    :type n: int
    :rtype: int
    """
    __ n __ 1:
      r.. 0
    ___ i __ r..(2, i..((n + 1) ** 0.5) + 1):
      __ n % i __ 0:
        r.. i + minSteps(n / i)
    r.. n

  ___ minSteps(self, n):
    ___ factor(n):
      d = 2
      w.... d * d <= n:
        w.... n % d __ 0:
          n /= d
          y.. d
        d += 1
      __ n > 1:
        y.. n

    r.. s..(factor(n))
