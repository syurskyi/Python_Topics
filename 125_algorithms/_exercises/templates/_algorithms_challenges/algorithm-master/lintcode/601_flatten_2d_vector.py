"""
Your Vector2D object will be instantiated and called as such:
i, v = Vector2D(vec2d), []
while i.hasNext(): v.append(i.next())
"""


c_ Vector2D:
    # @param vec2d {List[List[int]]}
    ___ - , vec2d):
        g = vec2d
        x = 0
        y = 0

    # @return {int} a next element
    ___ next
        __ n.. hasNext():
            r.. -1

        x = x
        y = y

        y += 1

        r.. g[x][y]

    # @return {boolean} true if it has next element
    # or false
    ___ hasNext
        w.... x < l..(g):
            __ y < l..(g[x]):
                r.. T..

            x += 1
            y = 0

        r.. F..
