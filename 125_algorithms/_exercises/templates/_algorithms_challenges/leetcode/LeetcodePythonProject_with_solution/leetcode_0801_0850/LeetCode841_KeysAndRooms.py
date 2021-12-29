'''
Created on Jan 30, 2019

@author: tongq
'''
class Solution(object):
    ___ canVisitAllRooms(self, rooms):
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
                        r.. True
        r.. l..(seen) __ l..(rooms)
    
    ___ test(self):
        testCases = [
            [[1],[2],[3],[]],
            [[1,3],[3,0,1],[2],[0]],
            [[2,3],[],[2],[1,3,1]],
            [[6,7,8],[5,4,9],[],[8],[4],[],[1,9,2,3],[7],[6,5],[2,3,1]],
        ]
        ___ rooms __ testCases:
            print('rooms: %s' % rooms)
            res = self.canVisitAllRooms(rooms)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
