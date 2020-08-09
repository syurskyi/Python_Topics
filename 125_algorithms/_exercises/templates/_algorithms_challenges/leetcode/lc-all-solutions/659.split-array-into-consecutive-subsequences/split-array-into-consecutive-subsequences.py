class Solution(object
  ___ isPossible(self, nums
    """
    :type nums: List[int]
    :rtype: bool
    """
    d = collections.defaultdict(list)
    ___ num in nums:
      __ d[num - 1]:
        heapq.heappush(d[num], heapq.heappop(d[num - 1]) + 1)
      ____
        heapq.heappush(d[num], 1)
    r_ not any(length < 3 ___ length in su.(d.values(), []))
