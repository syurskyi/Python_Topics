# find the largest end element in tails that is smaller than nums[i]
# and then replace it with nums[i] and discard the list in the same length
# which is implemented by `tail[idx] = num`

c_ Solution(o..
  ___ lengthOfLIS  nums
    """
    :type nums: List[int]
    :rtype: int
    """
    tail    # list
    ___ num __ nums:
      idx = bisect.bisect_left(tail, num)
      __ idx __ l..(tail
        tail.a..(num)
      ____:
        tail[idx] = num
    r.. l..(tail)
