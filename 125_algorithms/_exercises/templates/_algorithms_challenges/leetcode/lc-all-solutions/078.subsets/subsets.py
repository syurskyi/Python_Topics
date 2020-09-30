class Solution(object
  ___ subsets(self, nums
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    ___ dfs(nums, index, path, ans
      ans.append(path)
      [dfs(nums, i + 1, path + [nums[i]], ans) ___ i __ range(index, le.(nums))]

    ans =   # list
    dfs(nums, 0,   # list, ans)
    r_ ans
