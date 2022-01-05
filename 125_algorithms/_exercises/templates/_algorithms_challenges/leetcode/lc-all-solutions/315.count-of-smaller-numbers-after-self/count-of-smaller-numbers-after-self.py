_______ bisect


c_ Solution(o..):
  ___ countSmaller  nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans    # list
    bst    # list
    ___ num __ r..(nums):
      idx = bisect.bisect_left(bst, num)
      ans.a..(idx)
      bisect.insort(bst, num)
    r.. ans[::-1]
