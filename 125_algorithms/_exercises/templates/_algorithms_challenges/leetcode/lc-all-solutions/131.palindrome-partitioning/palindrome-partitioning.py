c_ Solution(object):
  ___ partition(self, s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    pal = [[F.. ___ i __ r..(0, l..(s))] ___ j __ r..(0, l..(s))]
    ans = [[[]]] + [[] ___ _ __ r..(l..(s))]

    ___ i __ r..(0, l..(s)):
      ___ j __ r..(0, i + 1):
        __ (s[j] __ s[i]) a.. ((j + 1 > i - 1) o. (pal[j + 1][i - 1])):
          pal[j][i] = T..
          ___ res __ ans[j]:
            a = res + [s[j:i + 1]]
            ans[i + 1].a..(a)
    r.. ans[-1]
