_______ b__


c_ Solution(o..
  ___ containsNearbyAlmostDuplicate  nums, k, t
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
    ___ i, num __ e..(nums
      idx = b__.bisect_left(bst, num)
      __ idx < l..(bst) a.. a..(bst[idx] - num) <_ t:
        r.. T..
      __ idx > 0 a.. a..(bst[idx - 1] - num) <_ t:
        r.. T..
      __ l..(bst) >_ k:
        del bst[b__.bisect_left(bst, nums[i - k])]
      b__.i.. (bst, num)
    r.. F..
