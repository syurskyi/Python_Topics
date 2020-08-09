class Solution:
  # @param board, a list of lists of 1 length string
  # @param word, a string
  # @return a boolean
  ___ exist(self, board, word
    # write your code here
    __ word __ "":
      r_ True
    __ le.(board) __ 0:
      r_ False
    visited = [[0] * le.(board[0]) for i in range(0, le.(board))]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    ___ dfs(i, j, board, visited, word, index
      __ word[index] != board[i][j]:
        r_ False
      __ le.(word) - 1 __ index:
        r_ True
      for direction in directions:
        ni, nj = i + direction[0], j + direction[1]
        __ ni >= 0 and ni < le.(board) and nj >= 0 and nj < le.(board[0]
          __ visited[ni][nj] __ 0:
            visited[ni][nj] = 1
            __ dfs(ni, nj, board, visited, word, index + 1
              r_ True
            visited[ni][nj] = 0
      r_ False

    for i in range(0, le.(board)):
      for j in range(0, le.(board[0])):
        visited[i][j] = 1
        __ dfs(i, j, board, visited, word, 0
          r_ True
        visited[i][j] = 0
    r_ False
