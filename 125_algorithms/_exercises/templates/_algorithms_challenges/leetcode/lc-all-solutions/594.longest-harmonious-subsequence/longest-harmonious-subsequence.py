class Solution(object
  ___ findLHS(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    d = collections.Counter(nums)
    ___ num __ nums:
      __ num + 1 __ d:
        ans = ma.(ans, d[num] + d[num + 1])
    r_ ans
