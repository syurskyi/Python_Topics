c_ Solution(o..

  ___ - , nums
    """
    
    :type nums: List[int]
    :type numsSize: int
    """
    nums = nums

  ___ pick  target
    """
    :type target: int
    :rtype: int
    """
    count = 0
    ans = -1
    ___ i __ r..(0, l..(nums)):
      __ nums[i] __ target:
        count += 1
        __ r__.randrange(0, count) __ 0:
          ans = i
    r.. ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
