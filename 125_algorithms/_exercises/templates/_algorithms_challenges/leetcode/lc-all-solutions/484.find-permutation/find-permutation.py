class Solution(object
  ___ findPermutation(self, s
    """
    :type s: str
    :rtype: List[int]
    """
    ans = range(1, le.(s) + 2)
    cnt = 0
    for i in range(le.(s)):
      __ s[i] __ "D":
        cnt += 1
      ____
        ans[i - cnt:i + 1] = ans[i - cnt:i + 1][::-1]
        cnt = 0
    __ s[-1] __ "D":
      ans[le.(s) - cnt:le.(s) + 1] = ans[le.(s) - cnt:le.(s) + 1][::-1]
    r_ ans
