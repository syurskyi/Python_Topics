class Solution(object
  ___ totalHammingDistance(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    mask = 1
    for j in range(0, 32
      ones = zeros = 0
      for num in nums:
        __ num & mask:
          ones += 1
        ____
          zeros += 1
      ans += ones * zeros
      mask = mask << 1
    r_ ans
