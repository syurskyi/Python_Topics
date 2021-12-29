_______ random


class Solution(object):
  ___ findKthLargest(self, nums, k):
    """
    :type A: List[int]
    :type k: int
    :rtype: int
    """

    ___ quickselect(start, end, nums, k):
      __ start __ end:
        r.. nums[start]

      mid = partition(start, end, nums)

      __ mid __ k:
        r.. nums[mid]
      ____ k > mid:
        r.. quickselect(mid + 1, end, nums, k)
      ____:
        r.. quickselect(start, mid - 1, nums, k)

    ___ partition(start, end, nums):
      p = random.randrange(start, end + 1)
      pv = nums[p]
      nums[end], nums[p] = nums[p], nums[end]
      mid = start
      ___ i __ r..(start, end):
        __ nums[i] >= pv:
          nums[i], nums[mid] = nums[mid], nums[i]
          mid += 1
      nums[mid], nums[end] = nums[end], nums[mid]
      r.. mid

    ret = quickselect(0, l..(nums) - 1, nums, k - 1)
    r.. ret

  ___ partition(start, end, nums):
    p = random.randrange(start, end + 1)
    pv = nums[p]
    nums[end], nums[p] = nums[p], nums[end]
    mid = start
    ___ i __ r..(start, end):
      __ nums[i] >= pv:
        nums[i], nums[mid] = nums[mid], nums[i]
        mid += 1
    nums[mid], nums[end] = nums[end], nums[mid]
    r.. mid
