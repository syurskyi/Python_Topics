'''
Created on Apr 30, 2018

@author: tongq
'''
c_ Solution(o..):
    ___ numBusesToDestination  routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        s, t = S, T
        __ s __ t: r.. 0
        hashmap    # dict
        ___ i __ r..(l..(routes)):
            ___ j __ r..(l..(routes[i])):
                __ routes[i][j] n.. __ hashmap:
                    hashmap[routes[i][j]]    # list
                hashmap[routes[i][j]].a..(i)
        queue    # list
        addedRoute = set()
        addedStop = set()
        ___ r __ hashmap[s]:
            __ r __ addedRoute: _____
            ___ i __ r..(l..(routes[r])):
                __ routes[r][i] n.. __ addedStop:
                    queue.a..(routes[r][i])
                    addedStop.add(routes[r][i])
            addedRoute.add(r)
        count = 0
        w.... queue:
            size = l..(queue)
            count += 1
            ___ _ __ r..(size):
                stop = queue.pop(0)
                __ stop __ t: r.. count
                ___ r __ hashmap[stop]:
                    __ r __ addedRoute: _____
                    ___ i __ r..(l..(routes[r])):
                        __ routes[r][i] n.. __ addedStop:
                            queue.a..(routes[r][i])
                    addedRoute.add(r)
        r.. -1
    
    ___ test
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
        ___ routes, s, t __ testCases:
            result = numBusesToDestination(routes, s, t)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
