c_ Solution:
  # @param {integer[]} nums
  # @return {string}
  ___ largestNumber  nums
    ___ cmpFunc(a, b
      stra, strb = s..(a), s..(b)
      __ stra + strb < strb + stra:
        r.. -1
      ____ stra + strb > strb + stra:
        r.. 1
      ____:
        r.. 0

    nums.s..(cmp=cmpFunc, r.._T..
    r.. "".j..(s..(num) ___ num __ nums) __ s..(nums) != 0 ____ "0"
