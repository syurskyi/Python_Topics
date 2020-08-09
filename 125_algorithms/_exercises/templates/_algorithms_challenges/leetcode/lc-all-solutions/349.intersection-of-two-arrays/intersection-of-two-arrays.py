class Solution(object
  ___ intersection(self, nums1, nums2
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    d = {}
    ans = []
    ___ num in nums1:
      d[num] = d.get(num, 0) + 1

    ___ num in nums2:
      __ num in d:
        ans.append(num)
        del d[num]
    r_ ans
