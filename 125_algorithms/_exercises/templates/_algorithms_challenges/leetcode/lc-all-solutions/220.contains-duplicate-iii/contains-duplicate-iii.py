_______ bisect


c_ Solution(object):
  ___ containsNearbyAlmostDuplicate  nums, k, t):
    """
    :type nums: List[int]
    :type k: int
    :type t: int
    :rtype: bool
    """
    __ k __ 0:
      r.. F..
    bst    # list
    __ k < 0 o. t < 0:
      r.. F..
    ___ i, num __ e..(nums):
      idx = bisect.bisect_left(bst, num)
      __ idx < l..(bst) a.. abs(bst[idx] - num) <= t:
        r.. T..
      __ idx > 0 a.. abs(bst[idx - 1] - num) <= t:
        r.. T..
      __ l..(bst) >= k:
        del bst[bisect.bisect_left(bst, nums[i - k])]
      bisect.insort(bst, num)
    r.. F..
