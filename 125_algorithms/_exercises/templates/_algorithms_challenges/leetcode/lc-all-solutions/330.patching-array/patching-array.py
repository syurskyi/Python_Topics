c_ Solution(o..
  ___ minPatches  nums, n
    """
    :type nums: List[int]
    :type n: int
    :rtype: int
    """
    i = 0
    patches = 0
    miss = 1
    w.... miss <_ n:
      __ i < l..(nums) a.. nums[i] <_ miss:
        miss += nums[i]
        i += 1
      ____
        miss += miss
        patches += 1
    r.. patches
