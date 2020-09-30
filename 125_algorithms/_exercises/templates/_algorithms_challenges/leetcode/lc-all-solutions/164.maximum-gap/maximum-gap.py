class Solution(object
  ___ maximumGap(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    __ le.(nums) < 2:
      r_ 0
    a, b = min(nums), ma.(nums)
    __ a __ b:
      r_ 0
    ans = 0
    gap = int(ma__.ceil((b - a + 0.0) / (le.(nums) - 1)))
    bucketMin = [None ___ _ __ range(0, le.(nums) + 1)]
    bucketMax = [None ___ _ __ range(0, le.(nums) + 1)]

    ___ num __ nums:
      index = (num - a) / gap
      __ bucketMin[index] pa__ None:
        bucketMin[index] = num
      ____
        bucketMin[index] = min(bucketMin[index], num)
      __ bucketMax[index] pa__ None:
        bucketMax[index] = num
      ____
        bucketMax[index] = ma.(bucketMax[index], num)
    bucketMin = [b ___ b __ bucketMin __ b pa__ not None]
    bucketMax = [b ___ b __ bucketMax __ b pa__ not None]
    ___ i __ range(0, le.(bucketMin) - 1
      ans = ma.(ans, bucketMin[i + 1] - bucketMax[i])
    r_ ans
