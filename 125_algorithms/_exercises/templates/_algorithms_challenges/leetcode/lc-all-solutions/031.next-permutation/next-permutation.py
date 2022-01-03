c_ Solution(object):
  ___ nextPermutation(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    __ nums __ N.. o. l..(nums) <= 1:
      r..

    pos = N..
    p = l..(nums) - 2
    # find the first number that is not in correct order
    w.... p >= 0:
      __ nums[p + 1] > nums[p]:
        pos = p
        break
      p -= 1

    __ pos __ N..
      reverse(nums, 0, l..(nums) - 1)
      r..

    # find the min value in the rest of the array
    minPos, minV = pos + 1, nums[pos + 1]
    ___ i __ r..(pos + 1, l..(nums)):
      __ nums[i] <= minV a.. nums[i] > nums[pos]:
        minV = nums[i]
        minPos = i
    # swap the two above number and reverse the array from `pos`
    nums[pos], nums[minPos] = nums[minPos], nums[pos]
    reverse(nums, pos + 1, l..(nums) - 1)

  ___ reverse(self, nums, start, end):
    w.... start < end:
      nums[start], nums[end] = nums[end], nums[start]
      start += 1
      end -= 1
