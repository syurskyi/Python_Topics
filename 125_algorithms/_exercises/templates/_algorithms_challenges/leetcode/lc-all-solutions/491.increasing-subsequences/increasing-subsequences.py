c_ Solution(o..):
  ___ findSubsequences  nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ans    # list

    ___ dfs(nums, start, path, ans):
      __ l..(path) >= 2:
        ans.a..(t..(path + []))

      ___ i __ r..(start, l..(nums)):
        __ i != start a.. nums[i] __ nums[i - 1]:
          _____
        __ path a.. nums[i] < path[-1]:
          _____
        path.a..(nums[i])
        dfs(nums, i + 1, path, ans)
        path.pop()

    dfs(nums, 0, [], ans)
    r.. l..(s..(ans))
