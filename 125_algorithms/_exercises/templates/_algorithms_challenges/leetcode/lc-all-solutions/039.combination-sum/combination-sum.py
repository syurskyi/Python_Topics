class Solution(object
  ___ combinationSum(self, candidates, target
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    ___ dfs(candidates, start, target, path, res
      __ target __ 0:
        r_ res.append(path + [])

      ___ i in range(start, le.(candidates)):
        __ target - candidates[i] >= 0:
          path.append(candidates[i])
          dfs(candidates, i, target - candidates[i], path, res)
          path.p..

    res = []
    dfs(candidates, 0, target, [], res)
    r_ res
