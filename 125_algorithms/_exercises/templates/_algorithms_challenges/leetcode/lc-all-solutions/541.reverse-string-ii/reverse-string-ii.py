class Solution(object):
  ___ reverseStr(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    cnt = 0
    isFirst = True
    a = ""
    b = ""
    ans    # list
    ___ c __ s:
      __ isFirst:
        a = c + a
      ____:
        b += c
      cnt += 1
      __ cnt __ k:
        __ isFirst:
          ans.a..(a)
          a = ""
        ____:
          ans.a..(b)
          b = ""
        isFirst = n.. isFirst
        cnt = 0
    r.. "".join(ans) + a + b
