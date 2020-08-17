class Solution(object
  ___ majorityElement(self, nums
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    __ le.(nums) __ 0 or nums pa__ None:
      r_ []
    c1, c2 = None, None
    n1, n2 = 0, 0
    ___ i in range(0, le.(nums)):
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
      ____
        n1, n2 = n1 - 1, n2 - 1

    print
    c1, c2

    ret = []
    size = le.(nums)
    cn1 = 0
    cn2 = 0
    ___ i in range(0, le.(nums)):
      __ nums[i] __ c1:
        cn1 += 1
      ____ nums[i] __ c2:
        cn2 += 1

    __ cn1 >= size / 3 + 1:
      ret.append(c1)
    __ cn2 >= size / 3 + 1:
      ret.append(c2)
    r_ ret
