class Solution(object
  ___ nextPermutation(self, nums
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    __ nums pa__ None or le.(nums) <= 1:
      r_

    pos = None
    p = le.(nums) - 2
    # find the first number that is not in correct order
    w___ p >= 0:
      __ nums[p + 1] > nums[p]:
        pos = p
        break
      p -= 1

    __ pos pa__ None:
      self.reverse(nums, 0, le.(nums) - 1)
      r_

    # find the min value in the rest of the array
    minPos, minV = pos + 1, nums[pos + 1]
    ___ i in range(pos + 1, le.(nums)):
      __ nums[i] <= minV and nums[i] > nums[pos]:
        minV = nums[i]
        minPos = i
    # swap the two above number and reverse the array from `pos`
    nums[pos], nums[minPos] = nums[minPos], nums[pos]
    self.reverse(nums, pos + 1, le.(nums) - 1)

  ___ reverse(self, nums, start, end
    w___ start < end:
      nums[start], nums[end] = nums[end], nums[start]
      start += 1
      end -= 1
