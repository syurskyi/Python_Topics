class Solution(object):
  ___ getPermutation(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    visited = [0 ___ i __ r..(n)]
    fact = [math.factorial(n - i - 1) ___ i __ r..(n)]
    ans = ""
    k -= 1
    ___ i __ r..(n):
      t = k / fact[i]
      ___ j __ r..(n):
        __ n.. visited[j]:
          __ t __ 0:
            break
          t -= 1
      ans += s..(j + 1)
      k %= fact[i]
      visited[j] = 1
    r.. ans
