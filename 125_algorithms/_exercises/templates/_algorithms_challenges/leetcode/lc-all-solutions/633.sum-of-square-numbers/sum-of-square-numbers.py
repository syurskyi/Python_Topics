class Solution(object):
  ___ judgeSquareSum(self, c):
    """
    :type c: int
    :rtype: bool
    """
    n = int(c ** 0.5)
    start = 0
    end = n
    w.... start <= end:
      mid = start ** 2 + end ** 2
      __ mid __ c:
        r.. True
      ____ mid < c:
        start += 1
      ____:
        end -= 1
    r.. False
