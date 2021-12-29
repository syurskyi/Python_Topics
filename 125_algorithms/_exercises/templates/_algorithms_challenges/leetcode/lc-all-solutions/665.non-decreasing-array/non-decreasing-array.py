class Solution(object):
  ___ checkPossibility(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    flag = False
    pre = float("-inf")
    ___ i __ r..(l..(nums) - 1):
      __ nums[i] < pre:
        __ nums[i + 1] >= nums[i - 1]:
          nums[i] = nums[i + 1]
        ____:
          nums[i - 1] = nums[i]
        flag = True
        break
      pre = nums[i]
    __ n.. flag and l..(nums) > 1 and nums[-1] < nums[-2]:
      nums[-1] = nums[-2]
    pre = float("-inf")
    ___ num __ nums:
      __ num < pre:
        r.. False
      pre = num
    r.. True
