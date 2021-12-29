class Solution(object):
  ___ convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    __ numRows <= 1:
      return s
    n = len(s)
    ans = []
    step = 2 * numRows - 2
    for i in range(numRows):
      one = i
      two = -i
      while one < n or two < n:
        __ 0 <= two < n and one != two and i != numRows - 1:
          ans.append(s[two])
        __ one < n:
          ans.append(s[one])
        one += step
        two += step
    return "".join(ans)
