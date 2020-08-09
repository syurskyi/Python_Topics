______ bisect


class Solution(object
  ___ containsNearbyAlmostDuplicate(self, nums, k, t
    """
    :type nums: List[int]
    :type k: int
    :type t: int
    :rtype: bool
    """
    __ k __ 0:
      r_ False
    bst = []
    __ k < 0 or t < 0:
      r_ False
    ___ i, num in enumerate(nums
      idx = bisect.bisect_left(bst, num)
      __ idx < le.(bst) and abs(bst[idx] - num) <= t:
        r_ True
      __ idx > 0 and abs(bst[idx - 1] - num) <= t:
        r_ True
      __ le.(bst) >= k:
        del bst[bisect.bisect_left(bst, nums[i - k])]
      bisect.insort(bst, num)
    r_ False
