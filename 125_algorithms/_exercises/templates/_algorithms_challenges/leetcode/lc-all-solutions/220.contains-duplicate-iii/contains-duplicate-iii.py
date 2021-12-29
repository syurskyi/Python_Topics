import bisect


class Solution(object):
  ___ containsNearbyAlmostDuplicate(self, nums, k, t):
    """
    :type nums: List[int]
    :type k: int
    :type t: int
    :rtype: bool
    """
    __ k == 0:
      return False
    bst = []
    __ k < 0 or t < 0:
      return False
    for i, num in enumerate(nums):
      idx = bisect.bisect_left(bst, num)
      __ idx < len(bst) and abs(bst[idx] - num) <= t:
        return True
      __ idx > 0 and abs(bst[idx - 1] - num) <= t:
        return True
      __ len(bst) >= k:
        del bst[bisect.bisect_left(bst, nums[i - k])]
      bisect.insort(bst, num)
    return False
