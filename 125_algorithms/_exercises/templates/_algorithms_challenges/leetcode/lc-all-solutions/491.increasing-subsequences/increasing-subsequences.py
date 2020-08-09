class Solution(object
  ___ findSubsequences(self, nums
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ans = []

    ___ dfs(nums, start, path, ans
      __ le.(path) >= 2:
        ans.append(tuple(path + []))

      ___ i in range(start, le.(nums)):
        __ i != start and nums[i] __ nums[i - 1]:
          continue
        __ path and nums[i] < path[-1]:
          continue
        path.append(nums[i])
        dfs(nums, i + 1, path, ans)
        path.pop()

    dfs(nums, 0, [], ans)
    r_ list(set(ans))
