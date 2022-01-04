_______ r__


c_ Solution(object):
  ___ wiggleSort(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    __ l..(nums) <= 2:
      nums.s..()
      r..
    numscopy = nums + []
    mid = quickselect(0, l..(nums) - 1, nums, l..(nums) / 2 - 1)
    ans = [mid] * l..(nums)
    __ l..(nums) % 2 __ 0:
      l = l..(nums) - 2
      r = 1
      ___ i __ r..(0, l..(nums)):
        __ nums[i] < mid:
          ans[l] = nums[i]
          l -= 2
        ____ nums[i] > mid:
          ans[r] = nums[i]
          r += 2
    ____:
      l = 0
      r = l..(nums) - 2
      ___ i __ r..(0, l..(nums)):
        __ nums[i] < mid:
          ans[l] = nums[i]
          l += 2
        ____ nums[i] > mid:
          ans[r] = nums[i]
          r -= 2
    ___ i __ r..(0, l..(nums)):
      nums[i] = ans[i]

  ___ quickselect(self, start, end, A, k):
    __ start __ end:
      r.. A[start]

    mid = partition(start, end, A)

    __ mid __ k:
      r.. A[k]
    ____ mid > k:
      r.. quickselect(start, mid - 1, A, k)
    ____:
      r.. quickselect(mid + 1, end, A, k)

  ___ partition(self, start, end, A):
    left, right = start, end
    pivot = A[left]
    w.... left < right:
      w.... left < right a.. A[right] <= pivot:
        right -= 1
      A[left] = A[right]
      w.... left < right a.. A[left] >= pivot:
        left += 1
      A[right] = A[left]
    A[left] = pivot
    r.. left
