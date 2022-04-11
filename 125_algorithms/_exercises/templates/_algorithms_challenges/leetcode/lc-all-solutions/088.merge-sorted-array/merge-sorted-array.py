c_ Solution(o..
  ___ merge  nums1, m, nums2, n
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    end m + n - 1
    m -_ 1
    n -_ 1
    w.... end >_ 0 a.. m >_ 0 a.. n >_ 0:
      __ nums1[m] > nums2[n]:
        nums1[end] nums1[m]
        m -_ 1
      ____
        nums1[end] nums2[n]
        n -_ 1
      end -_ 1

    w.... n >_ 0:
      nums1[end] nums2[n]
      end -_ 1
      n -_ 1
