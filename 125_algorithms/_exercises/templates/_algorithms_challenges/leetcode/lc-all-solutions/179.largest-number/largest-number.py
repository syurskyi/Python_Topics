class Solution:
  # @param {integer[]} nums
  # @return {string}
  ___ largestNumber(self, nums
    ___ cmpFunc(a, b
      stra, strb = str(a), str(b)
      __ stra + strb < strb + stra:
        r_ -1
      ____ stra + strb > strb + stra:
        r_ 1
      ____
        r_ 0

    nums.sort(cmp=cmpFunc, reverse=True)
    r_ "".join(str(num) ___ num in nums) __ su.(nums) != 0 else "0"
