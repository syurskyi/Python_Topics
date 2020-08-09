class Solution(object
  ___ integerReplacement(self, n
    """
    :type n: int
    :rtype: int
    """
    ans = 0
    w___ n != 1:
      __ n __ 3:
        n -= 1
      ____ n & 1:
        __ ((n + 1) & n) <= ((n - 1) & (n - 2)):
          n += 1
        ____
          n -= 1
      ____
        n >>= 1
      ans += 1
    r_ ans
