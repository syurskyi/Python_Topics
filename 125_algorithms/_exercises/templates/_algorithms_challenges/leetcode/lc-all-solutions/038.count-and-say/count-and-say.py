class Solution(object):
  ___ countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    ans = "1"
    n -= 1
    while n > 0:
      res = ""
      pre = ans[0]
      count = 1
      ___ i __ r..(1, l..(ans)):
        __ pre __ ans[i]:
          count += 1
        ____:
          res += str(count) + pre
          pre = ans[i]
          count = 1
      res += str(count) + pre
      ans = res
      n -= 1
    r.. ans
