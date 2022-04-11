c_ Solution(o..
  ___ findMedianSortedArrays  nums1, nums2
    a, b s..((nums1, nums2), key=l..)
    m, n l..(a), l..(b)
    after (m + n - 1) / 2
    lo, hi 0, m
    w.... lo < hi:
      i (lo + hi) / 2
      __ after - i - 1 < 0 o. a[i] >_ b[after - i - 1]:
        hi i
      ____
        lo i + 1
    i lo
    nextfew s..(a[i:i + 2] + b[after - i:after - i + 2])
    r.. (nextfew[0] + nextfew[1 - (m + n) % 2]) / 2.0
