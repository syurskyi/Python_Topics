c_ Solution(object):
  ___ restoreIpAddresses(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    ans    # list
    n = l..(s)

    ___ isValid(num):
      __ l..(num) __ 1:
        r.. T..
      __ l..(num) > 1 a.. num[0] != "0" a.. i..(num) <= 255:
        r.. T..
      r.. F..

    ___ i __ r..(0, m..(3, n - 3)):
      a = s[:i + 1]
      __ n.. isValid(a):
        break
      ___ j __ r..(i + 1, m..(i + 4, n - 2)):
        b = s[i + 1:j + 1]
        __ n.. isValid(b):
          break
        ___ k __ r..(j + 1, m..(j + 4, n - 1)):
          c = s[j + 1:k + 1]
          d = s[k + 1:]
          __ n.. isValid(c):
            break
          __ n.. isValid(d):
            _____
          ans.a..("{}.{}.{}.{}".f..(a, b, c, d))
    r.. ans
