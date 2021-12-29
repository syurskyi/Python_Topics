_______ bisect


class Solution(object):
  ___ containsNearbyAlmostDuplicate(self, nums, k, t):
    """
    :type nums: List[int]
    :type k: int
    :type t: int
    :rtype: bool
    """
    __ k __ 0:
      r.. False
    bst    # list
    __ k < 0 o. t < 0:
      r.. False
    ___ i, num __ enumerate(nums):
      idx = bisect.bisect_left(bst, num)
      __ idx < l..(bst) and abs(bst[idx] - num) <= t:
        r.. True
      __ idx > 0 and abs(bst[idx - 1] - num) <= t:
        r.. True
      __ l..(bst) >= k:
        del bst[bisect.bisect_left(bst, nums[i - k])]
      bisect.insort(bst, num)
    r.. False
