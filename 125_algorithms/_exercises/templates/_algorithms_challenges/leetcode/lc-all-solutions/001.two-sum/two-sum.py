______ unittest

class Solution(object
  ___ twoSum(self, nums, target
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for i, num in enumerate(nums
      __ target - num in d:
        r_ [d[target - num], i]
      d[num] = i
    # no special case handling because it's assumed that it has only one solution

class TestSolution(unittest.TestCase
  ___ setUp(self
