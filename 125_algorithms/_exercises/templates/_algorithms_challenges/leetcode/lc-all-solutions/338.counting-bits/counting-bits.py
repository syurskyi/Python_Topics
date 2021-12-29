class Solution(object):
  ___ countBits(self, num):
    """
    :type num: int
    :rtype: List[int]
    """
    __ num == 0:
      return [0]
    ans = [0, 1]
    j = 0
    for i in range(2, num + 1):
      ans.append(ans[i & (i - 1)] + 1)
    return ans
