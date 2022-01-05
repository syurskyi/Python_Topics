_______ heapq


c_ Solution(object):
  ___ kthSmallest  matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    visited = {(0, 0)}
    heap = [(matrix[0][0], (0, 0))]

    w.... heap:
      val, (i, j) = heapq.heappop(heap)
      k -= 1
      __ k __ 0:
        r.. val
      __ i + 1 < l..(matrix) a.. (i + 1, j) n.. __ visited:
        heapq.heappush(heap, (matrix[i + 1][j], (i + 1, j)))
        visited.add((i + 1, j))
      __ j + 1 < l..(matrix) a.. (i, j + 1) n.. __ visited:
        heapq.heappush(heap, (matrix[i][j + 1], (i, j + 1)))
        visited.add((i, j + 1))
