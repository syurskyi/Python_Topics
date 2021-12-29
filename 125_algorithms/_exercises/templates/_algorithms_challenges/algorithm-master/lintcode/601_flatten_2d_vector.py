"""
Your Vector2D object will be instantiated and called as such:
i, v = Vector2D(vec2d), []
while i.hasNext(): v.append(i.next())
"""


class Vector2D:
    # @param vec2d {List[List[int]]}
    ___ __init__(self, vec2d):
        self.g = vec2d
        self.x = 0
        self.y = 0

    # @return {int} a next element
    ___ next(self):
        __ not self.hasNext():
            return -1

        x = self.x
        y = self.y

        self.y += 1

        return self.g[x][y]

    # @return {boolean} true if it has next element
    # or false
    ___ hasNext(self):
        while self.x < len(self.g):
            __ self.y < len(self.g[self.x]):
                return True

            self.x += 1
            self.y = 0

        return False
