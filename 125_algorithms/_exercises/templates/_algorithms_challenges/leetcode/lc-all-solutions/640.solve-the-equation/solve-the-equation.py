class Solution(object
  ___ solveEquation(self, equation
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
    ___ param in left:
      param = param.replace("P", "+").replace("M", "-")
      __ param[-1] __ "x":
        k = 1
        __ le.(param) > 2:
          k = int(param[1:-1])
        __ param[0] __ "-":
          a -= k
        ____
          a += k
      ____
        b -= int(param)
    r_ "x={0}".format(str(b / a)) __ a else "No solution" __ b else "Infinite solutions"
