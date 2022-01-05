c_ Solution(object):
  ___ merge  nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    end = m + n - 1
    m -= 1
    n -= 1
    w.... end >= 0 a.. m >= 0 a.. n >= 0:
      __ nums1[m] > nums2[n]:
        nums1[end] = nums1[m]
        m -= 1
      ____:
        nums1[end] = nums2[n]
        n -= 1
      end -= 1

    w.... n >= 0:
      nums1[end] = nums2[n]
      end -= 1
      n -= 1
