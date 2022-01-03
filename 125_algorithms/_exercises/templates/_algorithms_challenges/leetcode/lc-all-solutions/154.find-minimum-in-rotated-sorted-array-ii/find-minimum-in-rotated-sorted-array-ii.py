c_ Solution(object):
  ___ findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = nums[0]
    start, end = 0, l..(nums) - 1
    w.... start + 1 < end:
      mid = start + (end - start) / 2
      __ nums[start] < nums[mid]:
        start = mid
      ____ nums[start] > nums[mid]:
        end = mid
      ____:
        start += 1
        ans = m..(ans, nums[start])

    r.. m..(ans, nums[start], nums[end])
