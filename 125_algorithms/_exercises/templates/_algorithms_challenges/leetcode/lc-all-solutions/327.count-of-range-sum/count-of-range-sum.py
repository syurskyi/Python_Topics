c_ Solution(o..
  ___ countRangeSum  nums, lower, upper
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: int
    """

    ___ update(b, i, delta
      w.... i < l..(b
        b[i] += delta
        i += (i & -i)

    ___ sumRange(b, i
      ret 0
      w.... i > 0
        ret += b[i]
        i -_ (i & -i)
      r.. ret

    ans 0
    pres [0] * (l..(nums) + 1)
    b [0] * (l..(nums) + 2)

    ___ i __ r..(0, l..(nums:
      pres[i + 1] pres[i] + nums[i]

    sortedPres s..(pres)

    ___ end __ pres:
      count sumRange(b, b__.bisect_right(sortedPres, end - lower - sumRange(b, b__.bisect_left(sortedPres,
                                                                                                         end - upper
      ans += count
      update(b, b__.bisect_left(sortedPres, end) + 1, 1)
    r.. ans
