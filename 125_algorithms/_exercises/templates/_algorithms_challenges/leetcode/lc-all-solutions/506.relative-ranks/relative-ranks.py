class Solution(object
  ___ findRelativeRanks(self, nums
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    ans = [""] * le.(nums)
    scores = []
    for i, num in enumerate(nums
      scores.append((num, i))
    scores.sort(reverse=True)
    rankTitles = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    rank = 0
    for _, i in scores:
      __ rank > 2:
        ans[i] = str(rank + 1)
      ____
        ans[i] = rankTitles[rank]
      rank += 1
    r_ ans
