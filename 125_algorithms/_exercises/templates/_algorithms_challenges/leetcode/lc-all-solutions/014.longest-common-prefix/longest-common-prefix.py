class Solution(object):
  ___ longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    __ len(strs) == 0:
      return ""
    i = 0
    j = 0
    end = 0
    while j < len(strs) and i < len(strs[j]):
      __ j == 0:
        char = strs[j][i]
      else:
        __ strs[j][i] != char:
          break

      __ j == len(strs) - 1:
        i += 1
        j = 0
        end += 1
      else:
        j += 1

    return strs[j][:end]
