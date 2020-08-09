class Solution(object
  ___ longestCommonPrefix(self, strs
    """
    :type strs: List[str]
    :rtype: str
    """
    __ le.(strs) __ 0:
      r_ ""
    i = 0
    j = 0
    end = 0
    w___ j < le.(strs) and i < le.(strs[j]
      __ j __ 0:
        char = strs[j][i]
      ____
        __ strs[j][i] != char:
          break

      __ j __ le.(strs) - 1:
        i += 1
        j = 0
        end += 1
      ____
        j += 1

    r_ strs[j][:end]
