class Solution(object
  ___ findMedianSortedArrays(self, nums1, nums2
    a, b = sorted((nums1, nums2), key=le.)
    m, n = le.(a), le.(b)
    after = (m + n - 1) / 2
    lo, hi = 0, m
    w___ lo < hi:
      i = (lo + hi) / 2
      __ after - i - 1 < 0 or a[i] >= b[after - i - 1]:
        hi = i
      ____
        lo = i + 1
    i = lo
    nextfew = sorted(a[i:i + 2] + b[after - i:after - i + 2])
    r_ (nextfew[0] + nextfew[1 - (m + n) % 2]) / 2.0
