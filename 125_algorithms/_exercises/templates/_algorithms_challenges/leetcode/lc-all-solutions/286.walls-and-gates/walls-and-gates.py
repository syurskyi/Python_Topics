____ c.. _______ d..

INF 2147483647


c_ Solution(o..
  ___ wallsAndGates  rooms
    """
    :type rooms: List[List[int]]
    :rtype: void Do not return anything, modify rooms in-place instead.
    """
    queue d..([])
    directions [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ___ i __ r..(0, l..(rooms:
      ___ j __ r..(0, l..(rooms[0]:
        __ rooms[i][j] __ 0:
          queue.a..((i, j

    w.... queue:
      i, j queue.popleft()
      ___ di, dj __ directions:
        p, q i + di, j + dj
        __ 0 <_ p < l..(rooms) a.. 0 <_ q < l..(rooms[0]) a.. rooms[p][q] __ INF:
          rooms[p][q] rooms[i][j] + 1
          queue.a..((p, q
