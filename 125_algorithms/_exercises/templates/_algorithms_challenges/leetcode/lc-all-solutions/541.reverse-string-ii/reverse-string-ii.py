c_ Solution(o..):
  ___ reverseStr  s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    cnt = 0
    isFirst = T..
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
    r.. "".j..(ans) + a + b
