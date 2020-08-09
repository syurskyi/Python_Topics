______ heapq


class Solution(object
  ___ kthSmallest(self, matrix, k
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    visited = {(0, 0)}
    heap = [(matrix[0][0], (0, 0))]

    w___ heap:
      val, (i, j) = heapq.heappop(heap)
      k -= 1
      __ k __ 0:
        r_ val
      __ i + 1 < le.(matrix) and (i + 1, j) not in visited:
        heapq.heappush(heap, (matrix[i + 1][j], (i + 1, j)))
        visited.add((i + 1, j))
      __ j + 1 < le.(matrix) and (i, j + 1) not in visited:
        heapq.heappush(heap, (matrix[i][j + 1], (i, j + 1)))
        visited.add((i, j + 1))
