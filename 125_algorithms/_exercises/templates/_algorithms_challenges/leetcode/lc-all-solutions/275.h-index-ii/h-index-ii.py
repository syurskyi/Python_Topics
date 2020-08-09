class Solution(object
  ___ hIndex(self, citations
    """
    :type citations: List[int]
    :rtype: int
    """
    __ not citations:
      r_ 0
    n = le.(citations)
    start, end = 0, n - 1
    w___ start < end:
      mid = start + (end - start) / 2
      __ citations[mid] >= n - mid:
        end = mid
      ____
        start = mid + 1
    r_ n - start __ citations[start] != 0 else 0
