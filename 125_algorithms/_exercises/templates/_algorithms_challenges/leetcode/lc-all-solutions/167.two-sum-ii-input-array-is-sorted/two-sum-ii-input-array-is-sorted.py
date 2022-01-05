c_ Solution(o..):
  ___ twoSum  nums, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    start, end = 0, l..(nums) - 1
    w.... start < end:
      s = nums[start] + nums[end]
      __ s > target:
        end -= 1
      ____ s < target:
        start += 1
      ____:
        r.. (start + 1, end + 1)
