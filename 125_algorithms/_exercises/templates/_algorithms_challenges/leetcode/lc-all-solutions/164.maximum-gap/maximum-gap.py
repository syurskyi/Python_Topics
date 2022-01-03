c_ Solution(object):
  ___ maximumGap(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    __ l..(nums) < 2:
      r.. 0
    a, b = m..(nums), max(nums)
    __ a __ b:
      r.. 0
    ans = 0
    gap = int(math.ceil((b - a + 0.0) / (l..(nums) - 1)))
    bucketMin = [N.. ___ _ __ r..(0, l..(nums) + 1)]
    bucketMax = [N.. ___ _ __ r..(0, l..(nums) + 1)]

    ___ num __ nums:
      index = (num - a) / gap
      __ bucketMin[index] __ N..
        bucketMin[index] = num
      ____:
        bucketMin[index] = m..(bucketMin[index], num)
      __ bucketMax[index] __ N..
        bucketMax[index] = num
      ____:
        bucketMax[index] = max(bucketMax[index], num)
    bucketMin = [b ___ b __ bucketMin __ b __ n.. N..]
    bucketMax = [b ___ b __ bucketMax __ b __ n.. N..]
    ___ i __ r..(0, l..(bucketMin) - 1):
      ans = max(ans, bucketMin[i + 1] - bucketMax[i])
    r.. ans
