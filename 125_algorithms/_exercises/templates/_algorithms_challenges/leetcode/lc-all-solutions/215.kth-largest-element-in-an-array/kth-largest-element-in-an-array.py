______ random


class Solution(object
  ___ findKthLargest(self, nums, k
    """
    :type A: List[int]
    :type k: int
    :rtype: int
    """

    ___ quickselect(start, end, nums, k
      __ start __ end:
        r_ nums[start]

      mid = partition(start, end, nums)

      __ mid __ k:
        r_ nums[mid]
      ____ k > mid:
        r_ quickselect(mid + 1, end, nums, k)
      ____
        r_ quickselect(start, mid - 1, nums, k)

    ___ partition(start, end, nums
      p = random.randrange(start, end + 1)
      pv = nums[p]
      nums[end], nums[p] = nums[p], nums[end]
      mid = start
      for i in range(start, end
        __ nums[i] >= pv:
          nums[i], nums[mid] = nums[mid], nums[i]
          mid += 1
      nums[mid], nums[end] = nums[end], nums[mid]
      r_ mid

    ret = quickselect(0, le.(nums) - 1, nums, k - 1)
    r_ ret

  ___ partition(start, end, nums
    p = random.randrange(start, end + 1)
    pv = nums[p]
    nums[end], nums[p] = nums[p], nums[end]
    mid = start
    for i in range(start, end
      __ nums[i] >= pv:
        nums[i], nums[mid] = nums[mid], nums[i]
        mid += 1
    nums[mid], nums[end] = nums[end], nums[mid]
    r_ mid
