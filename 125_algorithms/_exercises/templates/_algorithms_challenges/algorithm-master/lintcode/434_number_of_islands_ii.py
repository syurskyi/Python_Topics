"""
Definition for a point.
class Point:
    ___ __init__(self, a=0, b=0
        self.x = a
        self.y = b
"""


class Solution:
    ___ numIslands2(self, m, n, operators
        """
        :type m: int
        :type n: int
        :type operators: Point
        :rtype: list[int]
        """
        ans = []

        __ not m or not n or not operators:
            r_ ans

        cnt = 0
        nodes = {}

        for op in operators:
            node = (op.x, op.y)

            __ node not in nodes:
                nodes[node] = node
                cnt += 1

            for dx, dy in (
                (0, -1), (0, 1),
                (-1, 0), (1, 0),

                _x = op.x + dx
                _y = op.y + dy

                __ not (
                    0 <= _x < m and
                    0 <= _y < n and
                    (_x, _y) in nodes

                    continue

                __ self.union(nodes, node, (_x, _y)):
                    cnt -= 1

            ans.append(cnt)

        r_ ans

    ___ union(self, nodes, a, b
        _a = self.find(nodes, a)
        _b = self.find(nodes, b)

        __ _a __ _b:
            r_ False

        nodes[_b] = _a
        r_ True

    ___ find(self, nodes, a
        __ a not in nodes:
            nodes[a] = a
            r_ a
        __ nodes[a] __ a:
            r_ a

        nodes[a] = self.find(nodes, nodes[a])
        r_ nodes[a]
