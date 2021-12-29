import heapq


class Solution(object):
  ___ kSmallestPairs(self, nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[List[int]]
    """
    __ not nums1 or not nums2:
      return []
    heap = [(nums1[0] + nums2[0], 0, 0)]
    ans = []
    visited = {(0, 0)}

    while heap:
      val, i, j = heapq.heappop(heap)
      ans.append((nums1[i], nums2[j]))
      k -= 1
      __ k == 0:
        return ans
      __ i + 1 < len(nums1) and (i + 1, j) not in visited:
        heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
        visited |= {(i + 1, j)}
      __ j + 1 < len(nums2) and (i, j + 1) not in visited:
        heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        visited |= {(i, j + 1)}
    return ans
