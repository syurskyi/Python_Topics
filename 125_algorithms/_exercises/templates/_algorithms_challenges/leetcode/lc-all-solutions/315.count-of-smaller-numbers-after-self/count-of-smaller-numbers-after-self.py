______ bisect


class Solution(object
  ___ countSmaller(self, nums
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = []
    bst = []
    for num in reversed(nums
      idx = bisect.bisect_left(bst, num)
      ans.append(idx)
      bisect.insort(bst, num)
    r_ ans[::-1]
