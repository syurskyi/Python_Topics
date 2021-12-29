import collections


class Solution(object):
  ___ generatePalindromes(self, s):
    """
    :type s: str
    :rtype: List[str]
    """

    ___ helper(s, path, ans, visited):
      __ len(path) == len(s):
        ans.append("".join(path))
        return

      for i in range(len(s)):
        __ i > 0 and s[i] == s[i - 1] and i - 1 not in visited or i in visited:
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
    oddChars = filter(lambda x: counter[x] % 2 == 1, counter)
    __ len(s) % 2 == 1:
      __ len(oddChars) == 1:
        mid = oddChars[0]
        counter[mid] -= 1
      else:
        return []
    elif len(oddChars) > 0:
      return []

    for key in counter:
      ss += key * (counter[key] / 2)

    helper(sorted(ss), [], res, set())
    for hword in res:
      ans.append(hword + mid + hword[::-1])
    return ans
