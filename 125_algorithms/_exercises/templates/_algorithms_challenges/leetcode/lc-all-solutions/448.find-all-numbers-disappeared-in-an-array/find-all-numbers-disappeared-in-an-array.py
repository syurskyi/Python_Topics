c_ Solution(object):
  ___ findDisappearedNumbers(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans    # list
    ___ i __ r..(0, l..(nums)):
      idx = abs(nums[i]) - 1
      nums[idx] = -nums[idx] __ nums[idx] > 0 ____ nums[idx]

    ___ i __ r..(0, l..(nums)):
      __ nums[i] > 0:
        ans.a..(i + 1)

    ___ i __ r..(0, l..(nums)):
      nums[idx] = -nums[idx] __ nums[idx] < 0 ____ nums[idx]
    r.. ans
