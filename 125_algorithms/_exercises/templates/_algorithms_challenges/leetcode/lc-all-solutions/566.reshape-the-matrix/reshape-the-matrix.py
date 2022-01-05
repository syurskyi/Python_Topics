c_ Solution(o..):
  ___ matrixReshape  nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    __ r * c != l..(nums) * l..(nums[0]):
      r.. nums
    m = l..(nums)
    n = l..(nums[0])
    ans = [[0] * c ___ _ __ r..(r)]
    ___ i __ r..(r * c):
      ans[i / c][i % c] = nums[i / n][i % n]
    r.. ans
