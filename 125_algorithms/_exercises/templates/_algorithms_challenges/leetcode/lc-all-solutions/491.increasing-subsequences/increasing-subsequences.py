c_ Solution(object):
  ___ findSubsequences(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ans    # list

    ___ dfs(nums, start, path, ans):
      __ l..(path) >= 2:
        ans.a..(tuple(path + []))

      ___ i __ r..(start, l..(nums)):
        __ i != start a.. nums[i] __ nums[i - 1]:
          continue
        __ path a.. nums[i] < path[-1]:
          continue
        path.a..(nums[i])
        dfs(nums, i + 1, path, ans)
        path.pop()

    dfs(nums, 0, [], ans)
    r.. l..(set(ans))
