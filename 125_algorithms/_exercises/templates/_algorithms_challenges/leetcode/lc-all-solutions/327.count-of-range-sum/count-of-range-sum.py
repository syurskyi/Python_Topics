class Solution(object
  ___ countRangeSum(self, nums, lower, upper
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: int
    """

    ___ update(b, i, delta
      w___ i < le.(b
        b[i] += delta
        i += (i & -i)

    ___ sumRange(b, i
      ret = 0
      w___ i > 0:
        ret += b[i]
        i -= (i & -i)
      r_ ret

    ans = 0
    pres = [0] * (le.(nums) + 1)
    b = [0] * (le.(nums) + 2)

    ___ i in range(0, le.(nums)):
      pres[i + 1] = pres[i] + nums[i]

    sortedPres = sorted(pres)

    ___ end in pres:
      count = sumRange(b, bisect.bisect_right(sortedPres, end - lower)) - sumRange(b, bisect.bisect_left(sortedPres,
                                                                                                         end - upper))
      ans += count
      update(b, bisect.bisect_left(sortedPres, end) + 1, 1)
    r_ ans
