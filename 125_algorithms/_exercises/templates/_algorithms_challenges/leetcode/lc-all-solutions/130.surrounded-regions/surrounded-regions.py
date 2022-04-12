c_ UnionFind
  ___ - , m, n
    dad [i ___ i __ r..(0, m * n)]
    rank [0 ___ i __ r..(0, m * n)]
    m m
    n n

  ___ find  x
    dad dad
    __ dad[x] !_ x:
      dad[x] find(dad[x])
    r.. dad[x]

  ___ union  xy
    dad dad
    rank rank
    x, y map(find, xy)
    __ x __ y:
      r.. F..
    __ rank[x] > rank[y]:
      dad[y] x
    ____
      dad[x] y
      __ rank[x] __ rank[y]:
        rank[y] += 1
    r.. T..


c_ Solution:
  # @param {list[list[str]]} board a 2D board containing 'X' and 'O'
  # @return nothing 
  ___ solve  board
    # Write your code here
    __ l..(board) __ 0:
      r..
    regions s..([])
    n, m l..(board), l..(board 0
    uf UnionFind(l..(board 0, l..(board
    directions {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}
    ___ i __ r..(0, l..(board:
      ___ j __ r..(0, l..(board[0]:
        __ board[i][j] __ 'X':
          _____
        ___ d __ ["d", "r"]:
          di, dj directions[d]
          newi, newj i + di, j + dj
          __ newi >_ 0 a.. newi < l..(board) a.. newj >_ 0 a.. newj < l..(board[0]
            __ board[newi][newj] __ "O":
              uf.union((newi * m + newj, i * m + j

    ___ i __ r..(0, l..(board:
      ___ j __ [0, l..(board 0 - 1]:
        __ board[i][j] __ "O":
          regions.add(uf.find(i * m + j

    ___ j __ r..(0, l..(board[0]:
      ___ i __ [0, l..(board) - 1]:
        __ board[i][j] __ "O":
          regions.add(uf.find(i * m + j

    ___ i __ r..(0, l..(board:
      ___ j __ r..(0, l..(board[0]:
        __ board[i][j] __ "O" a.. uf.find(i * m + j) n.. __ regions:
          board[i][j] "X"
