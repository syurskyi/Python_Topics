class Solution(object
  ___ intersect(self, nums1, nums2
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    ans =   # list
    nums1.sort()
    nums2.sort()
    i = j = 0
    w___ i < le.(nums1) and j < le.(nums2
      __ nums1[i] < nums2[j]:
        i += 1
      ____ nums1[i] > nums2[j]:
        j += 1
      ____
        ans.append(nums1[i])
        i += 1
        j += 1

    r_ ans
