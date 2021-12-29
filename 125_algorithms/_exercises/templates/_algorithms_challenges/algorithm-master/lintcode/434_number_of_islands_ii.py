"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    ___ numIslands2(self, m, n, operators):
        """
        :type m: int
        :type n: int
        :type operators: Point
        :rtype: list[int]
        """
        ans = []

        __ not m or not n or not operators:
            return ans

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
            ):
                _x = op.x + dx
                _y = op.y + dy

                __ not (
                    0 <= _x < m and
                    0 <= _y < n and
                    (_x, _y) in nodes
                ):
                    continue

                __ self.union(nodes, node, (_x, _y)):
                    cnt -= 1

            ans.append(cnt)

        return ans

    ___ union(self, nodes, a, b):
        _a = self.find(nodes, a)
        _b = self.find(nodes, b)

        __ _a == _b:
            return False

        nodes[_b] = _a
        return True

    ___ find(self, nodes, a):
        __ a not in nodes:
            nodes[a] = a
            return a
        __ nodes[a] == a:
            return a

        nodes[a] = self.find(nodes, nodes[a])
        return nodes[a]
