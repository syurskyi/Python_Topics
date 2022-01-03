c_ Solution(object):
  ___ findPermutation(self, s):
    """
    :type s: str
    :rtype: List[int]
    """
    ans = r..(1, l..(s) + 2)
    cnt = 0
    ___ i __ r..(l..(s)):
      __ s[i] __ "D":
        cnt += 1
      ____:
        ans[i - cnt:i + 1] = ans[i - cnt:i + 1][::-1]
        cnt = 0
    __ s[-1] __ "D":
      ans[l..(s) - cnt:l..(s) + 1] = ans[l..(s) - cnt:l..(s) + 1][::-1]
    r.. ans
