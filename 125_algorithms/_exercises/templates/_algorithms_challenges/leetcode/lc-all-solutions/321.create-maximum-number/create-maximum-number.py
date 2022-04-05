c_ Solution(o..
  ___ maxNumber  _nums1, _nums2, k
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[int]
    """

    ___ getKDigits(num, k
      drop = l..(num) - k
      stack    # list
      ___ c __ num:
        w.... drop > 0 a.. stack a.. stack[-1] < c:
          stack.p.. )
          drop -_ 1
        stack.a..(c)
      r.. stack[:k]

    ___ merge(nums1, nums2
      ans    # list
      i = j = 0
      w.... i < l..(nums1) a.. j < l..(nums2
        __ nums1[i:] > nums2[j:]:
          ans.a..(nums1[i])
          i += 1
        ____
          ans.a..(nums2[j])
          j += 1

      __ i < l..(nums1
        ans += nums1[i:]
      __ j < l..(nums2
        ans += nums2[j:]
      r.. ans

    ans    # list
    ___ i __ r..(0, k + 1
      __ i <_ l..(_nums1) a.. k - i <_ l..(_nums2
        n1 = getKDigits(_nums1, i)
        n2 = getKDigits(_nums2, k - i)
        __ i __ 2:
          print
          n1, n2
        ans.a..(merge(n1, n2
    r.. m..(ans)
