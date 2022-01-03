c_ Solution(object):
  ___ largestRectangleArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    __ n.. height:
      r.. 0
    height.a..(-1)
    stack    # list
    ans = 0
    ___ i __ r..(0, l..(height)):
      w.... stack a.. height[i] < height[stack[-1]]:
        h = height[stack.pop()]
        w = i - stack[-1] - 1 __ stack ____ i
        ans = max(ans, h * w)
      stack.a..(i)
    height.pop()
    r.. ans
