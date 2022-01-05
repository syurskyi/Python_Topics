'''
Created on Jan 30, 2019

@author: tongq
'''
c_ Solution(object):
    ___ canVisitAllRooms  rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        dfs = [0]
        seen = set(dfs)
        w.... dfs:
            i = dfs.pop()
            ___ j __ rooms[i]:
                __ j n.. __ seen:
                    dfs.a..(j)
                    seen.add(j)
                    __ l..(seen) __ l..(rooms):
                        r.. T..
        r.. l..(seen) __ l..(rooms)
    
    ___ test
        testCases = [
            [[1],[2],[3],[]],
            [[1,3],[3,0,1],[2],[0]],
            [[2,3],[],[2],[1,3,1]],
            [[6,7,8],[5,4,9],[],[8],[4],[],[1,9,2,3],[7],[6,5],[2,3,1]],
        ]
        ___ rooms __ testCases:
            print('rooms: %s' % rooms)
            res = canVisitAllRooms(rooms)
            print('res: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
