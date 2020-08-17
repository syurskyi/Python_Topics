class Solution(object
  ___ subsetsWithDup(self, nums
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    ___ dfs(start, nums, path, res, visited
      res.append(path + [])

      ___ i in range(start, le.(nums)):
        __ start != i and nums[i] __ nums[i - 1]:
          continue
        __ i not in visited:
          visited[i] = 1
          path.append(nums[i])
          dfs(i + 1, nums, path, res, visited)
          path.p..
          del visited[i]

    nums.sort()
    res = []
    visited = {}
    dfs(0, nums, [], res, visited)
    r_ res
