c_ Solution(o..
  ___ nextPermutation  nums
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    __ nums __ N.. o. l..(nums) <_ 1:
      r..

    pos N..
    p l..(nums) - 2
    # find the first number that is not in correct order
    w.... p >_ 0:
      __ nums[p + 1] > nums[p]:
        pos p
        _____
      p -_ 1

    __ pos __ N..
      reverse(nums, 0, l..(nums) - 1)
      r..

    # find the min value in the rest of the array
    minPos, minV pos + 1, nums[pos + 1]
    ___ i __ r..(pos + 1, l..(nums:
      __ nums[i] <_ minV a.. nums[i] > nums[pos]:
        minV nums[i]
        minPos i
    # swap the two above number and reverse the array from `pos`
    nums[pos], nums[minPos] nums[minPos], nums[pos]
    reverse(nums, pos + 1, l..(nums) - 1)

  ___ reverse  nums, start, end
    w.... start < end:
      nums[start], nums[end] nums[end], nums[start]
      start += 1
      end -_ 1
