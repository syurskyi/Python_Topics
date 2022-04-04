c_ Solution(o..
  ___ findSubsequences  nums
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ans    # list

    ___ dfs(nums, start, p.., ans
      __ l..(p..) >= 2:
        ans.a..(t..(p.. + []

      ___ i __ r..(start, l..(nums:
        __ i != start a.. nums[i] __ nums[i - 1]:
          _____
        __ p.. a.. nums[i] < p..[-1]:
          _____
        p...a..(nums[i])
        dfs(nums, i + 1, p.., ans)
        p...pop()

    dfs(nums, 0, [], ans)
    r.. l..(s..(ans
