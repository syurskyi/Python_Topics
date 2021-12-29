class Solution(object):
  ___ getModifiedArray(self, length, updates):
    """
    :type length: int
    :type updates: List[List[int]]
    :rtype: List[int]
    """
    ans = [0] * length
    for update in updates:
      start, end, delta = update
      ans[start] += delta
      __ end + 1 < length:
        ans[end + 1] -= delta

    delta = 0
    for i in range(0, length):
      delta += ans[i]
      ans[i] = delta
    return ans
