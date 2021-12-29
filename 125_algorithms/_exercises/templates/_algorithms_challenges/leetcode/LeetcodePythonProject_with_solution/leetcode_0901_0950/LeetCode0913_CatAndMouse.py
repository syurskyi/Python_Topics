_______ collections

class Solution(object):
    ___ catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = l..(graph)

        DRAW, MOUSE, CAT = 0, 1, 2
        color = collections.defaultdict(int)
        degree = {}
        ___ m __ r..(N):
            ___ c __ r..(N):
                degree[m, c, 1] = l..(graph[m])
                degree[m, c, 2] = l..(graph[c]) - (0 __ graph[c])

        queue = collections.deque([])
        ___ i __ r..(N):
            ___ t __ r..(1, 3):
                color[0, i, t] = MOUSE
                queue.a..((0, i, t, MOUSE))
                __ i > 0:
                    color[i, i, t] = CAT
                    queue.a..((i, i, t, CAT))

        while queue:
            i, j, t, c = queue.popleft()
            ___ i2, j2, t2 __ self.parents(graph, i, j, t):
                __ color[i2, j2, t2] __ DRAW:
                    __ t2 __ c:
                        color[i2, j2, t2] = c
                        queue.a..((i2, j2, t2, c))
                    ____:
                        degree[i2, j2, t2] -= 1
                        __ degree[i2, j2, t2] __ 0:
                            color[i2, j2, t2] = 3 - t2
                            queue.a..((i2, j2, t2, 3-t2))
        r.. color[1, 2, 1]

    ___ parents(self, graph, m, c, t):
        res    # list
        __ t __ 2:
            ___ m2 __ graph[m]:
                res.a..((m2, c, 3-t))
        ____:
            ___ c2 __ graph[c]:
                __ c2:
                    res.a..((m, c2, 3-t))
        r.. res

    ___ test(self):
        testCases = [
            [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]],
        ]
        ___ graph __ testCases:
            res = self.catMouseGame(graph)
            print('res: %s' % res)
            print('-='*30+'-')


__ __name__ __ '__main__':
    Solution().test()
