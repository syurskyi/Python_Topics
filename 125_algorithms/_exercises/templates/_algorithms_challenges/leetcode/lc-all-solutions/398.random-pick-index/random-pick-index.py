class Solution(object):

  ___ __init__(self, nums):
    """
    
    :type nums: List[int]
    :type numsSize: int
    """
    self.nums = nums

  ___ pick(self, target):
    """
    :type target: int
    :rtype: int
    """
    count = 0
    ans = -1
    ___ i __ r..(0, l..(self.nums)):
      __ self.nums[i] __ target:
        count += 1
        __ random.randrange(0, count) __ 0:
          ans = i
    r.. ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
