class Solution(object
  ___ convert(self, s, numRows
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    __ numRows <= 1:
      r_ s
    n = le.(s)
    ans = []
    step = 2 * numRows - 2
    ___ i in range(numRows
      one = i
      two = -i
      w___ one < n or two < n:
        __ 0 <= two < n and one != two and i != numRows - 1:
          ans.append(s[two])
        __ one < n:
          ans.append(s[one])
        one += step
        two += step
    r_ "".join(ans)
