class Solution(object
  ___ findLHS(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    d = collections.Counter(nums)
    for num in nums:
      __ num + 1 in d:
        ans = max(ans, d[num] + d[num + 1])
    r_ ans
