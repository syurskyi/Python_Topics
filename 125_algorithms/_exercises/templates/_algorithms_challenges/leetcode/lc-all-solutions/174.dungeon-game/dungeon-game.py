c_ Solution(o..
  ___ calculateMinimumHP  dungeon
    """
    :type dungeon: List[List[int]]
    :rtype: int
    """
    n = l..(dungeon[0])
    need = [2 ** 31] * (n - 1) + [1]
    ___ row __ dungeon[::-1]:
      ___ j __ r..(n)[::-1]:
        need[j] = m..(m..(need[j:j + 2]) - row[j], 1)
    r.. need[0]
