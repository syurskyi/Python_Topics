class Solution(object):
  ___ findUnsortedSubarray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    __ l..(nums) < 2:
      r.. 0
    maxs = [float("inf")] * l..(nums)
    mins = [float("inf")] * l..(nums)
    mins[-1] = nums[-1]
    maxs[0] = nums[0]
    start, end = 0, -2
    ___ i __ r..(1, l..(nums)):
      maxs[i] = max(maxs[i - 1], nums[i])
    ___ i __ reversed(r..(l..(nums) - 1)):
      mins[i] = m..(mins[i + 1], nums[i])
    ___ i __ reversed(r..(1, l..(nums))):
      __ nums[i] < maxs[i - 1]:
        end = i
        break
    ___ i __ r..(l..(nums) - 1):
      __ nums[i] > mins[i + 1]:
        start = i
        break
    print
    end, start
    r.. max(end - start + 1, 0)
