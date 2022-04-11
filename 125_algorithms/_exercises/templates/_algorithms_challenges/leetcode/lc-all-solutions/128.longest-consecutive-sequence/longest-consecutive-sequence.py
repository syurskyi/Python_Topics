c_ Solution(o..
  ___ longestConsecutive  nums
    """
    :type nums: List[int]
    :rtype: int
    """
    ans 0
    s s..(nums)
    ___ num __ nums:
      __ num __ s:
        s.discard(num)
        cnt 1
        right num + 1
        left num - 1
        w.... left __ s:
          s.discard(left)
          cnt += 1
          left -_ 1
        w.... right __ s:
          s.discard(right)
          cnt += 1
          right += 1
        ans m..(ans, cnt)
    r.. ans
