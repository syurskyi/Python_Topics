class Solution(object
  ___ reverseStr(self, s, k
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    cnt = 0
    isFirst = True
    a = ""
    b = ""
    ans = []
    for c in s:
      __ isFirst:
        a = c + a
      ____
        b += c
      cnt += 1
      __ cnt __ k:
        __ isFirst:
          ans.append(a)
          a = ""
        ____
          ans.append(b)
          b = ""
        isFirst = not isFirst
        cnt = 0
    r_ "".join(ans) + a + b
