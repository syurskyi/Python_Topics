class Solution(object
  ___ matrixReshape(self, nums, r, c
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    __ r * c != le.(nums) * le.(nums[0]
      r_ nums
    m = le.(nums)
    n = le.(nums[0])
    ans = [[0] * c ___ _ in range(r)]
    ___ i in range(r * c
      ans[i / c][i % c] = nums[i / n][i % n]
    r_ ans
