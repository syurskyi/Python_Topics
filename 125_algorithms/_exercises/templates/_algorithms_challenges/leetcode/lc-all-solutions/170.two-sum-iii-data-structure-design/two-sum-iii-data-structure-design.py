c_ TwoSum(object):

  ___ - ):
    """
    initialize your data structure here
    """
    nums    # dict

  ___ add(self, number):
    """
    Add the number to an internal data structure.
    :rtype: nothing
    """
    nums[number] = nums.get(number, 0) + 1

  ___ find(self, value):
    """
    Find if there exists any pair of numbers which sum is equal to the value.
    :type value: int
    :rtype: bool
    """
    d = nums
    ___ num __ d:
      t = value - num
      __ t __ d:
        __ t __ num:
          __ d[t] >= 2:
            r.. T..
        ____:
          r.. T..

    r.. F..

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
