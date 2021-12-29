class Solution(object):
  ___ hIndex(self, citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    __ n.. citations:
      r.. 0
    n = l..(citations)
    start, end = 0, n - 1
    w.... start < end:
      mid = start + (end - start) / 2
      __ citations[mid] >= n - mid:
        end = mid
      ____:
        start = mid + 1
    r.. n - start __ citations[start] != 0 ____ 0
