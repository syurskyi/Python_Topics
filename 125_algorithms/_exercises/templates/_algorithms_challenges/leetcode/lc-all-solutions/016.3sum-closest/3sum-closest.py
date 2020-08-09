class Solution(object
  ___ threeSumClosest(self, nums, target
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    ans = 0
    diff = float("inf")
    ___ i in range(0, le.(nums)):
      start, end = i + 1, le.(nums) - 1
      w___ start < end:
        su. = nums[i] + nums[start] + nums[end]
        __ su. > target:
          __ abs(target - su.) < diff:
            diff = abs(target - su.)
            ans = su.
          end -= 1
        ____
          __ abs(target - su.) < diff:
            diff = abs(target - su.)
            ans = su.
          start += 1
    r_ ans
