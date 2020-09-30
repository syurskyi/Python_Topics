class Solution(object
  ___ minTotalDistance(self, grid
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    iList, jList, ppl =   # list, [], []
    ___ i __ range(0, le.(grid)):
      ___ j __ range(0, le.(grid[0])):
        __ grid[i][j] __ 1:
          ppl.append((i, j))
          iList.append(i)
          jList.append(j)
    jList.sort()
    m = (iList[le.(iList) / 2], jList[le.(jList) / 2])
    r_ su.(map(lambda p: abs(p[1] - m[1]) + abs(p[0] - m[0]), ppl))
