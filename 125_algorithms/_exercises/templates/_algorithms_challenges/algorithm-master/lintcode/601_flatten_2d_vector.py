"""
Your Vector2D object will be instantiated and called as such:
i, v = Vector2D(vec2d), []
w___ i.hasNext( v.append(i.next())
"""


class Vector2D:
    # @param vec2d {List[List[int]]}
    ___ __init__(self, vec2d
        self.g = vec2d
        self.x = 0
        self.y = 0

    # @return {int} a next element
    ___ next(self
        __ not self.hasNext(
            r_ -1

        x = self.x
        y = self.y

        self.y += 1

        r_ self.g[x][y]

    # @return {boolean} true if it has next element
    # or false
    ___ hasNext(self
        w___ self.x < le.(self.g
            __ self.y < le.(self.g[self.x]
                r_ True

            self.x += 1
            self.y = 0

        r_ False
