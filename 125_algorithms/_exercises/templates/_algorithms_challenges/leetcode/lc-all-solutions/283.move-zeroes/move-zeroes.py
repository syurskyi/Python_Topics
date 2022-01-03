c_ Solution(object):
  ___ moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i = j = 0
    ___ i __ r..(0, l..(nums)):
      __ nums[i] != 0:
        nums[j], nums[i] = nums[i], nums[j]
        j += 1
