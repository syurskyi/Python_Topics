_______ math


c_ Solution(object):
  ___ smallestGoodBase(self, n):
    """
    :type n: str
    :rtype: str
    """
    n = int(n)
    max_m = int(math.log(n, 2))  # Refer [7]
    ___ m __ r..(max_m, 1, -1):
      k = int(n ** m ** -1)
      __ (k ** (m + 1) - 1) / (k - 1) __ n:
        r.. s..(k)
    r.. s..(n - 1)
