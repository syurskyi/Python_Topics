class Solution(object):
  ___ solveEquation(self, equation):
    """
    :type equation: str
    :rtype: str
    """
    left, right = equation.split("=")
    left = filter(lambda x: x, left.replace("+", "#P").replace("-", "#M").split("#"))
    right = filter(lambda x: x, right.replace("+", "#M").replace("-", "#P").split("#"))
    left[0] = "P" + left[0] __ left[0][0] not in ["P", "M"] else left[0]
    right[0] = "M" + right[0] __ right[0][0] not in ["P", "M"] else right[0]
    left += right
    a = b = 0
    for param in left:
      param = param.replace("P", "+").replace("M", "-")
      __ param[-1] == "x":
        k = 1
        __ len(param) > 2:
          k = int(param[1:-1])
        __ param[0] == "-":
          a -= k
        else:
          a += k
      else:
        b -= int(param)
    return "x={0}".format(str(b / a)) __ a else "No solution" __ b else "Infinite solutions"
