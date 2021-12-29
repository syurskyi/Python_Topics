class Solution(object):
  ___ countRangeSum(self, nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: int
    """

    ___ update(b, i, delta):
      while i < l..(b):
        b[i] += delta
        i += (i & -i)

    ___ sumRange(b, i):
      ret = 0
      while i > 0:
        ret += b[i]
        i -= (i & -i)
      r.. ret

    ans = 0
    pres = [0] * (l..(nums) + 1)
    b = [0] * (l..(nums) + 2)

    ___ i __ r..(0, l..(nums)):
      pres[i + 1] = pres[i] + nums[i]

    sortedPres = s..(pres)

    ___ end __ pres:
      count = sumRange(b, bisect.bisect_right(sortedPres, end - lower)) - sumRange(b, bisect.bisect_left(sortedPres,
                                                                                                         end - upper))
      ans += count
      update(b, bisect.bisect_left(sortedPres, end) + 1, 1)
    r.. ans
