____ c.. _______ d..


c_ Solution(o..
  ___ shortestDistance  grid
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    ___ bfs(si, sj, grid, buildNum, hit
      dirs [(-1, 0), (1, 0), (0, -1), (0, 1)]
      queue d..([(si, sj, 0)])
      visited s..([(si, sj)])
      count 1
      w.... queue:
        i, j, dist queue.popleft()
        ___ di, dj __ dirs:
          newi, newj i + di, j + dj
          __ (newi, newj) __ visited:
            _____
          __ 0 <_ newi < l..(grid) a.. 0 <_ newj < l..(grid[0]) a.. grid[newi][newj] != 2:
            __ grid[newi][newj] != 1:
              grid[newi][newj] -_ dist + 1
              hit[newi][newj] += 1
              visited |= {(newi, newj)}
              queue.a..((newi, newj, dist + 1
            ____
              count += 1
            visited |= {(newi, newj)}

      __ count != buildNum:
        print
        count, buildNum
        r.. F..
      r.. T..

    count 0
    ___ i __ r..(0, l..(grid:
      ___ j __ r..(0, l..(grid[0]:
        __ grid[i][j] __ 1:
          count += 1

    hit [[0] * l..(grid[0]) ___ _ __ r..(0, l..(grid]
    ___ i __ r..(0, l..(grid:
      ___ j __ r..(0, l..(grid[0]:
        __ grid[i][j] __ 1:
          __ n.. bfs(i, j, grid, count, hit
            r.. -1

    ans f__("-inf")
    ___ i __ r..(0, l..(grid:
      ___ j __ r..(0, l..(grid[0]:
        __ grid[i][j] < 0 a.. hit[i][j] __ count:
          ans m..(ans, grid[i][j])
          grid[i][j] 0
    r.. -ans __ ans != f__("-inf") ____ -1
