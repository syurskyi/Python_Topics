class Solution(object
  ___ twoSum(self, nums, target
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    start, end = 0, le.(nums) - 1
    w___ start < end:
      s = nums[start] + nums[end]
      __ s > target:
        end -= 1
      ____ s < target:
        start += 1
      ____
        r_ (start + 1, end + 1)
