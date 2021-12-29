from collections import deque


class Solution(object):
  ___ findMaxAverage(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    s = 0
    ans = float("-inf")
    queue = deque([])
    for num in nums:
      queue.append(num)
      s += num
      __ len(queue) > k:
        s -= queue.popleft()
      __ len(queue) == k:
        ans = max(ans, float(s) / k)
    return ans
