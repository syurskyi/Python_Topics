"""
Your ZigzagIterator object will be instantiated and called as such:
solution, result = ZigzagIterator(v1, v2), []
w___ solution.hasNext( result.append(solution.next())
Output result
"""


class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    ___ __init__(self, v1, v2
        self.g = (v1, v2)
        self.x = 0
        self.y = 0
        self.max_y = max(le.(vec) for vec in self.g)

    """
    @return: An integer
    """
    ___ next(self
        __ not self.hasNext(
            r_ -1

        x = self.x
        y = self.y

        self.x += 1

        r_ self.g[x][y]

    """
    @return: True if has next
    """
    ___ hasNext(self
        w___ self.y < self.max_y:
            __ (
                self.x < le.(self.g) and
                self.y < le.(self.g[self.x])

                r_ True

            __ self.x >= le.(self.g
                self.x = 0
                self.y += 1

            __ self.y >= le.(self.g[self.x]
                self.x += 1

        r_ False


class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    ___ __init__(self, v1, v2
        self.queue = [vec for vec in (v1, v2) __ vec]

    """
    @return: An integer
    """
    ___ next(self
        __ not self.hasNext(
            r_ -1

        vec = self.queue.pop(0)
        val = vec.pop(0)

        __ vec:
            self.queue.append(vec)

        r_ val

    """
    @return: True if has next
    """
    ___ hasNext(self
        r_ bool(self.queue)
