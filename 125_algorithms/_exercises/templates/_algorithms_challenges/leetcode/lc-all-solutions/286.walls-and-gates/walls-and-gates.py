____ collections _______ deque

INF = 2147483647


class Solution(object):
  ___ wallsAndGates(self, rooms):
    """
    :type rooms: List[List[int]]
    :rtype: void Do not return anything, modify rooms in-place instead.
    """
    queue = deque([])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ___ i __ r..(0, l..(rooms)):
      ___ j __ r..(0, l..(rooms[0])):
        __ rooms[i][j] __ 0:
          queue.a..((i, j))

    w.... queue:
      i, j = queue.popleft()
      ___ di, dj __ directions:
        p, q = i + di, j + dj
        __ 0 <= p < l..(rooms) a.. 0 <= q < l..(rooms[0]) a.. rooms[p][q] __ INF:
          rooms[p][q] = rooms[i][j] + 1
          queue.a..((p, q))
