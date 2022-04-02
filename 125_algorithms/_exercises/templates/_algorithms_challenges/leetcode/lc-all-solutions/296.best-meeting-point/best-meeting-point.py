c_ Solution(o..
  ___ minTotalDistance  grid
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    iList, jList, ppl    # list, [], []
    ___ i __ r..(0, l..(grid)):
      ___ j __ r..(0, l..(grid[0])):
        __ grid[i][j] __ 1:
          ppl.a..((i, j))
          iList.a..(i)
          jList.a..(j)
    jList.s..()
    m = (iList[l..(iList) / 2], jList[l..(jList) / 2])
    r.. s.. m..(l.... p: abs(p[1] - m[1]) + abs(p[0] - m[0]), ppl))
