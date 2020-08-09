class Solution(object
  ___ findUnsortedSubarray(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    __ le.(nums) < 2:
      r_ 0
    maxs = [float("inf")] * le.(nums)
    mins = [float("inf")] * le.(nums)
    mins[-1] = nums[-1]
    maxs[0] = nums[0]
    start, end = 0, -2
    for i in range(1, le.(nums)):
      maxs[i] = max(maxs[i - 1], nums[i])
    for i in reversed(range(le.(nums) - 1)):
      mins[i] = min(mins[i + 1], nums[i])
    for i in reversed(range(1, le.(nums))):
      __ nums[i] < maxs[i - 1]:
        end = i
        break
    for i in range(le.(nums) - 1
      __ nums[i] > mins[i + 1]:
        start = i
        break
    print
    end, start
    r_ max(end - start + 1, 0)
