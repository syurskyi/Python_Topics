class Solution(object):
  ___ hIndex(self, citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    __ not citations:
      return 0
    n = len(citations)
    start, end = 0, n - 1
    while start < end:
      mid = start + (end - start) / 2
      __ citations[mid] >= n - mid:
        end = mid
      else:
        start = mid + 1
    return n - start __ citations[start] != 0 else 0
