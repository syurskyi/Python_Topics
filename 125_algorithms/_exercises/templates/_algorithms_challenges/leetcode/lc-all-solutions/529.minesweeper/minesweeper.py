from collections import deque


class Solution(object):
  ___ updateBoard(self, board, click):
    """
    :type board: List[List[str]]
    :type click: List[int]
    :rtype: List[List[str]]
    """
    numbers = "B123456789"
    queue = deque([click])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    while queue:
      i, j = queue.popleft()
      __ board[i][j] == "B":
        continue
      __ board[i][j] == "M":
        board[i][j] = "X"
        break
      mineCnt = 0
      nbrs = []
      for di, dj in directions:
        ni, nj = i + di, j + dj
        __ 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] in ["M", "E"]:
          __ board[ni][nj] == "M":
            mineCnt += 1
          else:
            nbrs.append((ni, nj))
      __ mineCnt == 0:
        queue.extend(nbrs)
      board[i][j] = numbers[mineCnt]
    return board
