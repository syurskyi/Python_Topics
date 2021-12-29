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
        ans    # list

        __ n.. m o. n.. n o. n.. operators:
            r.. ans

        cnt = 0
        nodes = {}

        ___ op __ operators:
            node = (op.x, op.y)

            __ node n.. __ nodes:
                nodes[node] = node
                cnt += 1

            ___ dx, dy __ (
                (0, -1), (0, 1),
                (-1, 0), (1, 0),
            ):
                _x = op.x + dx
                _y = op.y + dy

                __ n.. (
                    0 <= _x < m and
                    0 <= _y < n and
                    (_x, _y) __ nodes
                ):
                    continue

                __ self.union(nodes, node, (_x, _y)):
                    cnt -= 1

            ans.a..(cnt)

        r.. ans

    ___ union(self, nodes, a, b):
        _a = self.find(nodes, a)
        _b = self.find(nodes, b)

        __ _a __ _b:
            r.. False

        nodes[_b] = _a
        r.. True

    ___ find(self, nodes, a):
        __ a n.. __ nodes:
            nodes[a] = a
            r.. a
        __ nodes[a] __ a:
            r.. a

        nodes[a] = self.find(nodes, nodes[a])
        r.. nodes[a]
