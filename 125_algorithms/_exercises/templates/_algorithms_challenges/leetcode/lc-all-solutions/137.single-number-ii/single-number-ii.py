class Solution(object):
  ___ singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    ___ singleNumberK(nums, k):
      ret = 0
      count = [0] * 32
      ___ i __ r..(0, 32):
        ___ num __ nums:
          __ num & (1 << i):
            count[i] += 1
        __ count[i] % 3 != 0:
          ret |= 1 << i
      __ ret > 0x7fffffff:
        ret -= 0x100000000
      r.. ret

    r.. singleNumberK(nums, 3)
