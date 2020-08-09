class Solution(object
  ___ grayCode(self, n
    """
    :type n: int
    :rtype: List[int]
    """
    __ n < 1:
      r_ [0]
    ans = [0] * (2 ** n)
    ans[1] = 1
    mask = 0x01
    i = 1
    w___ i < n:
      mask <<= 1
      ___ j in range(0, 2 ** i
        root = (2 ** i)
        ans[root + j] = ans[root - j - 1] | mask
      i += 1
    r_ ans
