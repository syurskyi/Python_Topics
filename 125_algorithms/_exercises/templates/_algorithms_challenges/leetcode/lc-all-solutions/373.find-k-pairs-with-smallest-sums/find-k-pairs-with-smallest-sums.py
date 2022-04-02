_______ heapq


c_ Solution(o..
  ___ kSmallestPairs  nums1, nums2, k
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[List[int]]
    """
    __ n.. nums1 o. n.. nums2:
      r.. []
    heap = [(nums1[0] + nums2[0], 0, 0)]
    ans    # list
    visited = {(0, 0)}

    w.... heap:
      val, i, j = heapq.heappop(heap)
      ans.a..((nums1[i], nums2[j]))
      k -= 1
      __ k __ 0:
        r.. ans
      __ i + 1 < l..(nums1) a.. (i + 1, j) n.. __ visited:
        heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
        visited |= {(i + 1, j)}
      __ j + 1 < l..(nums2) a.. (i, j + 1) n.. __ visited:
        heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        visited |= {(i, j + 1)}
    r.. ans
