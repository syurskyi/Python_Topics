______ collections


class Solution(object
  ___ generatePalindromes(self, s
    """
    :type s: str
    :rtype: List[str]
    """

    ___ helper(s, path, ans, visited
      __ le.(path) __ le.(s
        ans.append("".join(path))
        r_

      for i in range(le.(s)):
        __ i > 0 and s[i] __ s[i - 1] and i - 1 not in visited or i in visited:
          continue
        visited |= {i}
        path.append(s[i])
        helper(s, path, ans, visited)
        path.pop()
        visited -= {i}

    ans = []
    res = []
    ss = ""
    mid = ""
    counter = collections.Counter(s)
    oddChars = filter(lambda x: counter[x] % 2 __ 1, counter)
    __ le.(s) % 2 __ 1:
      __ le.(oddChars) __ 1:
        mid = oddChars[0]
        counter[mid] -= 1
      ____
        r_ []
    ____ le.(oddChars) > 0:
      r_ []

    for key in counter:
      ss += key * (counter[key] / 2)

    helper(sorted(ss), [], res, set())
    for hword in res:
      ans.append(hword + mid + hword[::-1])
    r_ ans
