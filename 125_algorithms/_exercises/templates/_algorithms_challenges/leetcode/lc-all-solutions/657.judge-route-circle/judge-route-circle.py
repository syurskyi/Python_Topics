c_ Solution(o..
  ___ judgeCircle  moves
    """
    :type moves: str
    :rtype: bool
    """
    x y 0
    dirs {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    ___ move __ moves:
      dx, dy dirs[move]
      x += dx
      y += dy
    r.. x __ y __ 0
