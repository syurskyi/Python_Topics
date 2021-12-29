class TwoSum(object):

  ___ __init__(self):
    """
    initialize your data structure here
    """
    self.nums = {}

  ___ add(self, number):
    """
    Add the number to an internal data structure.
    :rtype: nothing
    """
    self.nums[number] = self.nums.get(number, 0) + 1

  ___ find(self, value):
    """
    Find if there exists any pair of numbers which sum is equal to the value.
    :type value: int
    :rtype: bool
    """
    d = self.nums
    ___ num __ d:
      t = value - num
      __ t __ d:
        __ t __ num:
          __ d[t] >= 2:
            r.. True
        ____:
          r.. True

    r.. False

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
