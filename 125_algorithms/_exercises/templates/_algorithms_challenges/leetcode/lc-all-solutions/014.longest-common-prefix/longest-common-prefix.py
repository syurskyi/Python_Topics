c_ Solution(o..
  ___ longestCommonPrefix  strs
    """
    :type strs: List[str]
    :rtype: str
    """
    __ l..(strs) __ 0:
      r.. ""
    i 0
    j 0
    end 0
    w.... j < l..(strs) a.. i < l..(strs[j]
      __ j __ 0:
        char strs[j][i]
      ____
        __ strs[j][i] !_ char:
          _____

      __ j __ l..(strs) - 1:
        i += 1
        j 0
        end += 1
      ____
        j += 1

    r.. strs[j][:end]
