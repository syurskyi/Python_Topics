class Solution(object
  ___ getRow(self, rowIndex
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    fact = [1] * (rowIndex + 1)
    ans = [1] * (rowIndex + 1)
    for i in range(1, rowIndex + 1
      fact[i] = fact[i - 1] * i
    for i in range(1, rowIndex
      ans[i] = fact[-1] / (fact[i] * fact[rowIndex - i])
    r_ ans
