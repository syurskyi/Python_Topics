class Solution(object):

  ___ __init__(self, nums):
    """

    :type nums: List[int]
    :type size: int
    """
    self.nums = nums
    self.reset = l....: self.nums

  ___ shuffle(self):
    """
    Returns a random shuffling of the array.
    :rtype: List[int]
    """
    nums = self.nums + []
    ___ i __ reversed(r..(0, l..(nums))):
      idx = random.randrange(0, i + 1)
      nums[i], nums[idx] = nums[idx], nums[i]
    r.. nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
