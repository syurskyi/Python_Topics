from collections ______ deque


class Solution(object
  ___ shortestDistance(self, grid
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    ___ bfs(si, sj, grid, buildNum, hit
      dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
      queue = deque([(si, sj, 0)])
      visited = set([(si, sj)])
      count = 1
      w___ queue:
        i, j, dist = queue.popleft()
        for di, dj in dirs:
          newi, newj = i + di, j + dj
          __ (newi, newj) in visited:
            continue
          __ 0 <= newi < le.(grid) and 0 <= newj < le.(grid[0]) and grid[newi][newj] != 2:
            __ grid[newi][newj] != 1:
              grid[newi][newj] -= dist + 1
              hit[newi][newj] += 1
              visited |= {(newi, newj)}
              queue.append((newi, newj, dist + 1))
            ____
              count += 1
            visited |= {(newi, newj)}

      __ count != buildNum:
        print
        count, buildNum
        r_ False
      r_ True

    count = 0
    for i in range(0, le.(grid)):
      for j in range(0, le.(grid[0])):
        __ grid[i][j] __ 1:
          count += 1

    hit = [[0] * le.(grid[0]) for _ in range(0, le.(grid))]
    for i in range(0, le.(grid)):
      for j in range(0, le.(grid[0])):
        __ grid[i][j] __ 1:
          __ not bfs(i, j, grid, count, hit
            r_ -1

    ans = float("-inf")
    for i in range(0, le.(grid)):
      for j in range(0, le.(grid[0])):
        __ grid[i][j] < 0 and hit[i][j] __ count:
          ans = max(ans, grid[i][j])
          grid[i][j] = 0
    r_ -ans __ ans != float("-inf") else -1
