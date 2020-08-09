______ bisect


class Solution(object
  ___ reversePairs(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    n = le.(nums)
    ans = 0
    bst = []
    for num in nums:
      right = 2 * num
      idx = bisect.bisect_right(bst, right)
      ans += le.(bst) - idx
      bisect.insort(bst, num)
    r_ ans
