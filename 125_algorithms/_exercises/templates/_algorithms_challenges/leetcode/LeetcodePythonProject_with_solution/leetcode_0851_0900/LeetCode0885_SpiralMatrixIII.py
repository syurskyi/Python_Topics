'''
Created on Oct 16, 2019

@author: tongq
'''
c_ Solution(object):
    ___ spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        res    # list
        dx, dy, n = 0, 1, 0
        w.... l..(res) < R*C:
            ___ _ __ r..(n//2+1):
                __ 0 <= r0 < R a.. 0 <= c0 < C:
                    res.a..([r0, c0])
                r0, c0 = r0+dx, c0+dy
            dx, dy, n = dy, -dx, n+1
        r.. res
    
    ___ spiralMatrixIII_own(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        pos = [r0, c0]
        res    # list
        length = 1
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        i = 0
        w.... l..(res) < R*C:
            ___ _ __ r..(2):
                ___ _ __ r..(length):
                    __ isInRange(pos, R, C):
                        res.a..(pos)
                    d = dirs[i%4]
                    pos = [pos[0]+d[0], pos[1]+d[1]]
                i += 1
            length += 1
        r.. res
    
    ___ isInRange(self, pos, R, C):
        r.. 0 <= pos[0] < R a.. 0 <= pos[1] < C
    
    ___ test
        testCases = [
            [1, 4, 0, 0],
        ]
        ___ R, C, r0, c0 __ testCases:
            res = spiralMatrixIII(R, C, r0, c0)
            print('res: %s' % res)

__ __name__ __ '__main__':
    Solution().test()
