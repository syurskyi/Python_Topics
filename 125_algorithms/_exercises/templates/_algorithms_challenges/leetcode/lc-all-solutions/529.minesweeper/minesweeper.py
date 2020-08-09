from collections ______ deque


class Solution(object
  ___ updateBoard(self, board, click
    """
    :type board: List[List[str]]
    :type click: List[int]
    :rtype: List[List[str]]
    """
    numbers = "B123456789"
    queue = deque([click])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    w___ queue:
      i, j = queue.popleft()
      __ board[i][j] __ "B":
        continue
      __ board[i][j] __ "M":
        board[i][j] = "X"
        break
      mineCnt = 0
      nbrs = []
      ___ di, dj in directions:
        ni, nj = i + di, j + dj
        __ 0 <= ni < le.(board) and 0 <= nj < le.(board[0]) and board[ni][nj] in ["M", "E"]:
          __ board[ni][nj] __ "M":
            mineCnt += 1
          ____
            nbrs.append((ni, nj))
      __ mineCnt __ 0:
        queue.extend(nbrs)
      board[i][j] = numbers[mineCnt]
    r_ board
