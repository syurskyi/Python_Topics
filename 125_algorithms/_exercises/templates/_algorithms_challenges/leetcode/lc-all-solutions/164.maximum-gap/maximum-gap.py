class Solution(object
  ___ maximumGap(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    __ le.(nums) < 2:
      r_ 0
    a, b = min(nums), max(nums)
    __ a __ b:
      r_ 0
    ans = 0
    gap = int(ma__.ceil((b - a + 0.0) / (le.(nums) - 1)))
    bucketMin = [None ___ _ in range(0, le.(nums) + 1)]
    bucketMax = [None ___ _ in range(0, le.(nums) + 1)]

    ___ num in nums:
      index = (num - a) / gap
      __ bucketMin[index] is None:
        bucketMin[index] = num
      ____
        bucketMin[index] = min(bucketMin[index], num)
      __ bucketMax[index] is None:
        bucketMax[index] = num
      ____
        bucketMax[index] = max(bucketMax[index], num)
    bucketMin = [b ___ b in bucketMin __ b is not None]
    bucketMax = [b ___ b in bucketMax __ b is not None]
    ___ i in range(0, le.(bucketMin) - 1
      ans = max(ans, bucketMin[i + 1] - bucketMax[i])
    r_ ans
