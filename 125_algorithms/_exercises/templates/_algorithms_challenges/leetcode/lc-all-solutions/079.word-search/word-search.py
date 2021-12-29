class Solution:
  # @param board, a list of lists of 1 length string
  # @param word, a string
  # @return a boolean
  ___ exist(self, board, word):
    # write your code here
    __ word __ "":
      r.. True
    __ l..(board) __ 0:
      r.. False
    visited = [[0] * l..(board[0]) ___ i __ r..(0, l..(board))]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    ___ dfs(i, j, board, visited, word, index):
      __ word[index] != board[i][j]:
        r.. False
      __ l..(word) - 1 __ index:
        r.. True
      ___ direction __ directions:
        ni, nj = i + direction[0], j + direction[1]
        __ ni >= 0 and ni < l..(board) and nj >= 0 and nj < l..(board[0]):
          __ visited[ni][nj] __ 0:
            visited[ni][nj] = 1
            __ dfs(ni, nj, board, visited, word, index + 1):
              r.. True
            visited[ni][nj] = 0
      r.. False

    ___ i __ r..(0, l..(board)):
      ___ j __ r..(0, l..(board[0])):
        visited[i][j] = 1
        __ dfs(i, j, board, visited, word, 0):
          r.. True
        visited[i][j] = 0
    r.. False
