c_ Solution(object):
  ___ firstMissingPositive  nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    w.... i < l..(nums):
      __ 0 < nums[i] <= l..(nums) a.. nums[nums[i] - 1] != nums[i]:
        nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
      ____:
        i += 1

    ___ i __ r..(0, l..(nums)):
      __ nums[i] != i + 1:
        r.. i + 1
    r.. l..(nums) + 1
