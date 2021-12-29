class UnionFind():
  ___ __init__(self, m, n):
    self.dad = [i ___ i __ r..(0, m * n)]
    self.rank = [0 ___ i __ r..(0, m * n)]
    self.m = m
    self.n = n

  ___ find(self, x):
    dad = self.dad
    __ dad[x] != x:
      dad[x] = self.find(dad[x])
    r.. dad[x]

  ___ union(self, xy):
    dad = self.dad
    rank = self.rank
    x, y = map(self.find, xy)
    __ x __ y:
      r.. False
    __ rank[x] > rank[y]:
      dad[y] = x
    ____:
      dad[x] = y
      __ rank[x] __ rank[y]:
        rank[y] += 1
    r.. True


class Solution:
  # @param {list[list[str]]} board a 2D board containing 'X' and 'O'
  # @return nothing 
  ___ solve(self, board):
    # Write your code here
    __ l..(board) __ 0:
      r..
    regions = set([])
    n, m = l..(board), l..(board[0])
    uf = UnionFind(l..(board[0]), l..(board))
    directions = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}
    ___ i __ r..(0, l..(board)):
      ___ j __ r..(0, l..(board[0])):
        __ board[i][j] __ 'X':
          continue
        ___ d __ ["d", "r"]:
          di, dj = directions[d]
          newi, newj = i + di, j + dj
          __ newi >= 0 and newi < l..(board) and newj >= 0 and newj < l..(board[0]):
            __ board[newi][newj] __ "O":
              uf.union((newi * m + newj, i * m + j))

    ___ i __ r..(0, l..(board)):
      ___ j __ [0, l..(board[0]) - 1]:
        __ board[i][j] __ "O":
          regions.add(uf.find(i * m + j))

    ___ j __ r..(0, l..(board[0])):
      ___ i __ [0, l..(board) - 1]:
        __ board[i][j] __ "O":
          regions.add(uf.find(i * m + j))

    ___ i __ r..(0, l..(board)):
      ___ j __ r..(0, l..(board[0])):
        __ board[i][j] __ "O" and uf.find(i * m + j) n.. __ regions:
          board[i][j] = "X"
