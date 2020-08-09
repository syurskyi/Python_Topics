class Solution(object
  ___ findMaxConsecutiveOnes(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    count = 0
    for num in nums:
      __ num __ 1:
        count += 1
      ____
        count = 0
      ans = max(ans, count)
    r_ ans
