class Solution(object
  ___ restoreIpAddresses(self, s
    """
    :type s: str
    :rtype: List[str]
    """
    ans = []
    n = le.(s)

    ___ isValid(num
      __ le.(num) __ 1:
        r_ True
      __ le.(num) > 1 and num[0] != "0" and int(num) <= 255:
        r_ True
      r_ False

    ___ i in range(0, min(3, n - 3)):
      a = s[:i + 1]
      __ not isValid(a
        break
      ___ j in range(i + 1, min(i + 4, n - 2)):
        b = s[i + 1:j + 1]
        __ not isValid(b
          break
        ___ k in range(j + 1, min(j + 4, n - 1)):
          c = s[j + 1:k + 1]
          d = s[k + 1:]
          __ not isValid(c
            break
          __ not isValid(d
            continue
          ans.append("{}.{}.{}.{}".format(a, b, c, d))
    r_ ans
