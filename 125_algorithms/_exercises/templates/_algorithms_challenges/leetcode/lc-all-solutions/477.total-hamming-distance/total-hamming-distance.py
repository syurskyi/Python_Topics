class Solution(object
  ___ totalHammingDistance(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    mask = 1
    ___ j in range(0, 32
      ones = zeros = 0
      ___ num in nums:
        __ num & mask:
          ones += 1
        ____
          zeros += 1
      ans += ones * zeros
      mask = mask << 1
    r_ ans
