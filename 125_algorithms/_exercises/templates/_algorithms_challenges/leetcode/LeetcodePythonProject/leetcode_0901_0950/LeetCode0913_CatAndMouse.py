______ collections

class Solution(object
    ___ catMouseGame(self, graph
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = le.(graph)

        DRAW, MOUSE, CAT = 0, 1, 2
        color = collections.defaultdict(int)
        degree = {}
        ___ m in range(N
            ___ c in range(N
                degree[m, c, 1] = le.(graph[m])
                degree[m, c, 2] = le.(graph[c]) - (0 in graph[c])

        queue = collections.deque([])
        ___ i in range(N
            ___ t in range(1, 3
                color[0, i, t] = MOUSE
                queue.append((0, i, t, MOUSE))
                __ i > 0:
                    color[i, i, t] = CAT
                    queue.append((i, i, t, CAT))

        w___ queue:
            i, j, t, c = queue.popleft()
            ___ i2, j2, t2 in self.parents(graph, i, j, t
                __ color[i2, j2, t2] pa__ DRAW:
                    __ t2 __ c:
                        color[i2, j2, t2] = c
                        queue.append((i2, j2, t2, c))
                    ____
                        degree[i2, j2, t2] -= 1
                        __ degree[i2, j2, t2] __ 0:
                            color[i2, j2, t2] = 3 - t2
                            queue.append((i2, j2, t2, 3-t2))
        r_ color[1, 2, 1]

    ___ parents(self, graph, m, c, t
        res = []
        __ t __ 2:
            ___ m2 in graph[m]:
                res.append((m2, c, 3-t))
        ____
            ___ c2 in graph[c]:
                __ c2:
                    res.append((m, c2, 3-t))
        r_ res

    ___ test(self
        testCases = [
            [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]],
        ]
        ___ graph in testCases:
            res = self.catMouseGame(graph)
            print('res: %s' % res)
            print('-='*30+'-')


__ __name__ __ '__main__':
    Solution().test()
