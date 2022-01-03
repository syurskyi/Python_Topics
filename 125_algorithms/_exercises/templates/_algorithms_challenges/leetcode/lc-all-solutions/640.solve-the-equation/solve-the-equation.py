c_ Solution(object):
  ___ solveEquation(self, equation):
    """
    :type equation: str
    :rtype: str
    """
    left, right = equation.s..("=")
    left = filter(l.... x: x, left.r..("+", "#P").r..("-", "#M").s..("#"))
    right = filter(l.... x: x, right.r..("+", "#M").r..("-", "#P").s..("#"))
    left[0] = "P" + left[0] __ left[0][0] n.. __ ["P", "M"] ____ left[0]
    right[0] = "M" + right[0] __ right[0][0] n.. __ ["P", "M"] ____ right[0]
    left += right
    a = b = 0
    ___ param __ left:
      param = param.r..("P", "+").r..("M", "-")
      __ param[-1] __ "x":
        k = 1
        __ l..(param) > 2:
          k = int(param[1:-1])
        __ param[0] __ "-":
          a -= k
        ____:
          a += k
      ____:
        b -= int(param)
    r.. "x={0}".f..(s..(b / a)) __ a ____ "No solution" __ b ____ "Infinite solutions"
