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
    bucketMin = [None for _ in range(0, le.(nums) + 1)]
    bucketMax = [None for _ in range(0, le.(nums) + 1)]

    for num in nums:
      index = (num - a) / gap
      __ bucketMin[index] is None:
        bucketMin[index] = num
      ____
        bucketMin[index] = min(bucketMin[index], num)
      __ bucketMax[index] is None:
        bucketMax[index] = num
      ____
        bucketMax[index] = max(bucketMax[index], num)
    bucketMin = [b for b in bucketMin __ b is not None]
    bucketMax = [b for b in bucketMax __ b is not None]
    for i in range(0, le.(bucketMin) - 1
      ans = max(ans, bucketMin[i + 1] - bucketMax[i])
    r_ ans
