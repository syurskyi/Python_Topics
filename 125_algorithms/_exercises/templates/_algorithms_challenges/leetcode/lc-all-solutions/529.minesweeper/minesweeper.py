____ collections _______ deque


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
    w.... queue:
      i, j = queue.popleft()
      __ board[i][j] __ "B":
        continue
      __ board[i][j] __ "M":
        board[i][j] = "X"
        break
      mineCnt = 0
      nbrs    # list
      ___ di, dj __ directions:
        ni, nj = i + di, j + dj
        __ 0 <= ni < l..(board) a.. 0 <= nj < l..(board[0]) a.. board[ni][nj] __ ["M", "E"]:
          __ board[ni][nj] __ "M":
            mineCnt += 1
          ____:
            nbrs.a..((ni, nj))
      __ mineCnt __ 0:
        queue.extend(nbrs)
      board[i][j] = numbers[mineCnt]
    r.. board
