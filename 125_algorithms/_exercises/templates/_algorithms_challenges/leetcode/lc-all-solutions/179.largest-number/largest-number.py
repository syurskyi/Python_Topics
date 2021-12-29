class Solution:
  # @param {integer[]} nums
  # @return {string}
  ___ largestNumber(self, nums):
    ___ cmpFunc(a, b):
      stra, strb = str(a), str(b)
      __ stra + strb < strb + stra:
        r.. -1
      ____ stra + strb > strb + stra:
        r.. 1
      ____:
        r.. 0

    nums.sort(cmp=cmpFunc, r.._T..
    r.. "".join(str(num) ___ num __ nums) __ s..(nums) != 0 ____ "0"
