class Solution(object
  ___ combinationSum2(self, candidates, target
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    ___ dfs(nums, target, start, visited, path, res
      __ target __ 0:
        res.append(path + [])
        r_

      for i in range(start, le.(nums)):
        __ i > start and nums[i] __ nums[i - 1]:
          continue
        __ target - nums[i] < 0:
          r_ 0
        __ i not in visited:
          visited.add(i)
          path.append(nums[i])
          dfs(nums, target - nums[i], i + 1, visited, path, res)
          path.pop()
          visited.discard(i)

    candidates.sort()
    res = []
    visited = set([])
    dfs(candidates, target, 0, visited, [], res)
    r_ res
