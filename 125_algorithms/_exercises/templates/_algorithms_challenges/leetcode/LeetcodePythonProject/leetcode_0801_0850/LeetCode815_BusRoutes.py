'''
Created on Apr 30, 2018

@author: tongq
'''
class Solution(object
    ___ numBusesToDestination(self, routes, S, T
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        s, t = S, T
        __ s __ t: r_ 0
        hashmap = {}
        ___ i in range(le.(routes)):
            ___ j in range(le.(routes[i])):
                __ routes[i][j] not in hashmap:
                    hashmap[routes[i][j]] = []
                hashmap[routes[i][j]].append(i)
        queue = []
        addedRoute = set()
        addedStop = set()
        ___ r in hashmap[s]:
            __ r in addedRoute: continue
            ___ i in range(le.(routes[r])):
                __ routes[r][i] not in addedStop:
                    queue.append(routes[r][i])
                    addedStop.add(routes[r][i])
            addedRoute.add(r)
        count = 0
        w___ queue:
            size = le.(queue)
            count += 1
            ___ _ in range(size
                stop = queue.pop(0)
                __ stop __ t: r_ count
                ___ r in hashmap[stop]:
                    __ r in addedRoute: continue
                    ___ i in range(le.(routes[r])):
                        __ routes[r][i] not in addedStop:
                            queue.append(routes[r][i])
                    addedRoute.add(r)
        r_ -1
    
    ___ test(self
        testCases = [
            [
                [[1, 2, 7], [3, 6, 7]],
                1, 6,
            ], # 2
            [
                [[7,12],[4,5,15],[6],[15,19],[9,12,13]],
                15,12
            ],
        ]
        ___ routes, s, t in testCases:
            result = self.numBusesToDestination(routes, s, t)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
