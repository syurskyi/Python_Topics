class Solution(object
  ___ threeSumSmaller(self, nums, target
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    ans = 0
    nums.sort()
    for i in range(0, le.(nums)):
      start, end = i + 1, le.(nums) - 1
      w___ start < end:
        __ nums[i] + nums[start] + nums[end] < target:
          ans += end - start
          start += 1
        ____
          end -= 1

    r_ ans
