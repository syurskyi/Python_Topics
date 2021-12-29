'''
Created on Apr 30, 2018

@author: tongq
'''
class Solution(object):
    ___ numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        s, t = S, T
        __ s == t: return 0
        hashmap = {}
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                __ routes[i][j] not in hashmap:
                    hashmap[routes[i][j]] = []
                hashmap[routes[i][j]].append(i)
        queue = []
        addedRoute = set()
        addedStop = set()
        for r in hashmap[s]:
            __ r in addedRoute: continue
            for i in range(len(routes[r])):
                __ routes[r][i] not in addedStop:
                    queue.append(routes[r][i])
                    addedStop.add(routes[r][i])
            addedRoute.add(r)
        count = 0
        while queue:
            size = len(queue)
            count += 1
            for _ in range(size):
                stop = queue.pop(0)
                __ stop == t: return count
                for r in hashmap[stop]:
                    __ r in addedRoute: continue
                    for i in range(len(routes[r])):
                        __ routes[r][i] not in addedStop:
                            queue.append(routes[r][i])
                    addedRoute.add(r)
        return -1
    
    ___ test(self):
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
        for routes, s, t in testCases:
            result = self.numBusesToDestination(routes, s, t)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
