class Vector2D(object

  ___ __init__(self, vec2d
    """
    Initialize your data structure here.
    :type vec2d: List[List[int]]
    """
    self.x = self.y = 0
    self.m = vec2d

  ___ next(self
    """
    :rtype: int
    """
    self.y += 1
    r_ self.m[self.x][self.y - 1]

  ___ hasNext(self
    """
    :rtype: bool
    """
    m = self.m
    w___ self.x < le.(m) and self.y >= le.(m[self.x]
      self.x += 1
      self.y = 0
    r_ self.x < le.(m)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# w___ i.hasNext( v.append(i.next())
