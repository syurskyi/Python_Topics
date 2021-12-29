class Solution(object):
  ___ maxNumber(self, _nums1, _nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[int]
    """

    ___ getKDigits(num, k):
      drop = len(num) - k
      stack = []
      for c in num:
        while drop > 0 and stack and stack[-1] < c:
          stack.pop()
          drop -= 1
        stack.append(c)
      return stack[:k]

    ___ merge(nums1, nums2):
      ans = []
      i = j = 0
      while i < len(nums1) and j < len(nums2):
        __ nums1[i:] > nums2[j:]:
          ans.append(nums1[i])
          i += 1
        else:
          ans.append(nums2[j])
          j += 1

      __ i < len(nums1):
        ans += nums1[i:]
      __ j < len(nums2):
        ans += nums2[j:]
      return ans

    ans = []
    for i in range(0, k + 1):
      __ i <= len(_nums1) and k - i <= len(_nums2):
        n1 = getKDigits(_nums1, i)
        n2 = getKDigits(_nums2, k - i)
        __ i == 2:
          print
          n1, n2
        ans.append(merge(n1, n2))
    return max(ans)
