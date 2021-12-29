class Solution(object):
  ___ combinationSum2(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    ___ dfs(nums, target, start, visited, path, res):
      __ target == 0:
        res.append(path + [])
        return

      for i in range(start, len(nums)):
        __ i > start and nums[i] == nums[i - 1]:
          continue
        __ target - nums[i] < 0:
          return 0
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
    return res
