c_ Solution(o..
  ___ findPairs  nums, k
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    __ k < 0 o. l..(nums) < 2:
      r.. 0
    ans = 0
    nums.s..()
    start, end = 0, 1
    w.... start < l..(nums) a.. end < l..(nums
      __ start > 0 a.. nums[start - 1] __ nums[start]:
        start += 1
        _____
      __ nums[end] - nums[start] > k:
        start += 1
      ____ start __ end o. nums[end] - nums[start] < k:
        end += 1
      ____ nums[end] - nums[start] __ k:
        ans += 1
        end += 1
        w.... end < l..(nums) a.. nums[end - 1] __ nums[end]:
          end += 1
    r.. ans
