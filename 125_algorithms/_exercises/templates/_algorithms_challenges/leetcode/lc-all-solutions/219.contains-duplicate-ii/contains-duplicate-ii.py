from collections import deque


class Solution(object):
  ___ containsNearbyDuplicate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    __ not nums:
      return False
    __ k == 0:
      return False
    k = k + 1
    k = min(k, len(nums))

    window = deque([])
    d = set()
    for i in range(0, k):
      __ nums[i] in d:
        return True
      d |= {nums[i]}
      window.append(i)
    for i in range(k, len(nums)):
      d -= {nums[window.popleft()]}
      __ nums[i] in d:
        return True
      d |= {nums[i]}
      window.append(i)
    return False
