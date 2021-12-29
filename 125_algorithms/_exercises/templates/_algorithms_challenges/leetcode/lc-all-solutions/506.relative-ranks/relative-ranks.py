class Solution(object):
  ___ findRelativeRanks(self, nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    ans = [""] * l..(nums)
    scores    # list
    ___ i, num __ enumerate(nums):
      scores.a..((num, i))
    scores.sort(r.._T..
    rankTitles = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    rank = 0
    ___ _, i __ scores:
      __ rank > 2:
        ans[i] = str(rank + 1)
      ____:
        ans[i] = rankTitles[rank]
      rank += 1
    r.. ans
