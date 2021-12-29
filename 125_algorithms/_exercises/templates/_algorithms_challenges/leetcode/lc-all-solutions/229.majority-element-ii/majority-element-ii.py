class Solution(object):
  ___ majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    __ l..(nums) __ 0 o. nums __ N..
      r.. []
    c1, c2 = N.., N..
    n1, n2 = 0, 0
    ___ i __ r..(0, l..(nums)):
      __ c1 __ nums[i]:
        n1 += 1
      ____ c2 __ nums[i]:
        n2 += 1
      ____ n1 __ 0:
        c1 = nums[i]
        n1 += 1
      ____ n2 __ 0:
        c2 = nums[i]
        n2 += 1
      ____:
        n1, n2 = n1 - 1, n2 - 1

    print
    c1, c2

    ret    # list
    size = l..(nums)
    cn1 = 0
    cn2 = 0
    ___ i __ r..(0, l..(nums)):
      __ nums[i] __ c1:
        cn1 += 1
      ____ nums[i] __ c2:
        cn2 += 1

    __ cn1 >= size / 3 + 1:
      ret.a..(c1)
    __ cn2 >= size / 3 + 1:
      ret.a..(c2)
    r.. ret
