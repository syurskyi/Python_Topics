c_ Solution:
  # @param board, a list of lists of 1 length string
  # @param word, a string
  # @return a boolean
  ___ exist  board, word
    # write your code here
    __ word __ "":
      r.. T..
    __ l..(board) __ 0:
      r.. F..
    visited = [[0] * l..(board[0]) ___ i __ r..(0, l..(board))]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    ___ dfs(i, j, board, visited, word, index
      __ word[index] != board[i][j]:
        r.. F..
      __ l..(word) - 1 __ index:
        r.. T..
      ___ direction __ directions:
        ni, nj = i + direction[0], j + direction[1]
        __ ni >= 0 a.. ni < l..(board) a.. nj >= 0 a.. nj < l..(board[0]
          __ visited[ni][nj] __ 0:
            visited[ni][nj] = 1
            __ dfs(ni, nj, board, visited, word, index + 1
              r.. T..
            visited[ni][nj] = 0
      r.. F..

    ___ i __ r..(0, l..(board)):
      ___ j __ r..(0, l..(board[0])):
        visited[i][j] = 1
        __ dfs(i, j, board, visited, word, 0
          r.. T..
        visited[i][j] = 0
    r.. F..
