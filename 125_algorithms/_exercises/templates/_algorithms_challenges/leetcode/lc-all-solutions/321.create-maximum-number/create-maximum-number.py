class Solution(object
  ___ maxNumber(self, _nums1, _nums2, k
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[int]
    """

    ___ getKDigits(num, k
      drop = le.(num) - k
      stack = []
      ___ c in num:
        w___ drop > 0 and stack and stack[-1] < c:
          stack.p..
          drop -= 1
        stack.append(c)
      r_ stack[:k]

    ___ merge(nums1, nums2
      ans = []
      i = j = 0
      w___ i < le.(nums1) and j < le.(nums2
        __ nums1[i:] > nums2[j:]:
          ans.append(nums1[i])
          i += 1
        ____
          ans.append(nums2[j])
          j += 1

      __ i < le.(nums1
        ans += nums1[i:]
      __ j < le.(nums2
        ans += nums2[j:]
      r_ ans

    ans = []
    ___ i in range(0, k + 1
      __ i <= le.(_nums1) and k - i <= le.(_nums2
        n1 = getKDigits(_nums1, i)
        n2 = getKDigits(_nums2, k - i)
        __ i __ 2:
          print
          n1, n2
        ans.append(merge(n1, n2))
    r_ max(ans)
