c_ Solution(o..
  ___ countAndSay  n
    """
    :type n: int
    :rtype: str
    """
    ans = "1"
    n -_ 1
    w.... n > 0:
      res = ""
      pre = ans[0]
      count = 1
      ___ i __ r..(1, l..(ans:
        __ pre __ ans[i]:
          count += 1
        ____
          res += s..(count) + pre
          pre = ans[i]
          count = 1
      res += s..(count) + pre
      ans = res
      n -_ 1
    r.. ans
