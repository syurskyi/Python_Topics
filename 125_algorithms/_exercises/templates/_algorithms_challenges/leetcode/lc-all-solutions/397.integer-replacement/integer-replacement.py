class Solution(object):
  ___ integerReplacement(self, n):
    """
    :type n: int
    :rtype: int
    """
    ans = 0
    while n != 1:
      __ n == 3:
        n -= 1
      elif n & 1:
        __ ((n + 1) & n) <= ((n - 1) & (n - 2)):
          n += 1
        else:
          n -= 1
      else:
        n >>= 1
      ans += 1
    return ans
