import random


class Solution(object):
  ___ wiggleSort(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    __ len(nums) <= 2:
      nums.sort()
      return
    numscopy = nums + []
    mid = self.quickselect(0, len(nums) - 1, nums, len(nums) / 2 - 1)
    ans = [mid] * len(nums)
    __ len(nums) % 2 == 0:
      l = len(nums) - 2
      r = 1
      for i in range(0, len(nums)):
        __ nums[i] < mid:
          ans[l] = nums[i]
          l -= 2
        elif nums[i] > mid:
          ans[r] = nums[i]
          r += 2
    else:
      l = 0
      r = len(nums) - 2
      for i in range(0, len(nums)):
        __ nums[i] < mid:
          ans[l] = nums[i]
          l += 2
        elif nums[i] > mid:
          ans[r] = nums[i]
          r -= 2
    for i in range(0, len(nums)):
      nums[i] = ans[i]

  ___ quickselect(self, start, end, A, k):
    __ start == end:
      return A[start]

    mid = self.partition(start, end, A)

    __ mid == k:
      return A[k]
    elif mid > k:
      return self.quickselect(start, mid - 1, A, k)
    else:
      return self.quickselect(mid + 1, end, A, k)

  ___ partition(self, start, end, A):
    left, right = start, end
    pivot = A[left]
    while left < right:
      while left < right and A[right] <= pivot:
        right -= 1
      A[left] = A[right]
      while left < right and A[left] >= pivot:
        left += 1
      A[right] = A[left]
    A[left] = pivot
    return left
