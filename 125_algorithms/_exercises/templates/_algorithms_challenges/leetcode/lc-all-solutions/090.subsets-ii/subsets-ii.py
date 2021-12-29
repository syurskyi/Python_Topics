class Solution(object):
  ___ subsetsWithDup(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    ___ dfs(start, nums, path, res, visited):
      res.a..(path + [])

      ___ i __ r..(start, l..(nums)):
        __ start != i a.. nums[i] __ nums[i - 1]:
          continue
        __ i n.. __ visited:
          visited[i] = 1
          path.a..(nums[i])
          dfs(i + 1, nums, path, res, visited)
          path.pop()
          del visited[i]

    nums.s..()
    res    # list
    visited = {}
    dfs(0, nums, [], res, visited)
    r.. res
