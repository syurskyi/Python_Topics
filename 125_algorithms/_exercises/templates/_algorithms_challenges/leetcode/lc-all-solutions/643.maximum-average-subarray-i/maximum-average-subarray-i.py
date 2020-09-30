from collections ______ deque


class Solution(object
  ___ findMaxAverage(self, nums, k
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    s = 0
    ans = float("-inf")
    queue = deque(  # list)
    ___ num __ nums:
      queue.append(num)
      s += num
      __ le.(queue) > k:
        s -= queue.popleft()
      __ le.(queue) __ k:
        ans = ma.(ans, float(s) / k)
    r_ ans
