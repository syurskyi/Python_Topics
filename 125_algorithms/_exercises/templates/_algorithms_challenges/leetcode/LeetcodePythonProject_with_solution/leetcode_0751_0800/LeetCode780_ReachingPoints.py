'''
Created on Apr 8, 2018

@author: tongq
'''
c_ Solution(o..
    ___ reachingPoints  sx, sy, tx, ty
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        w.... sx < tx a.. sy < ty:
            tx, ty = tx%ty, ty%tx
        __ sx __ tx a.. (ty-sy) % sx __ 0 o.\
            sy __ ty a.. (tx-sx) % sy __ 0:
            r.. T..
        ____:
            r.. F..
    
    # RuntimeError: maximum recursion depth exceeded
    ___ reachingPoints_own  sx, sy, tx, ty
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        mem    # dict
        r.. helper(sx, sy, tx, ty, mem)
    
    ___ helper  sx, sy, tx, ty, mem
        __ sx __ tx a.. sy __ ty:
            mem[(sx, sy)] = T..
            r.. T..
        __ sx > tx o. sy > ty:
            mem[(sx, sy)] = F..
            r.. F..
        __ (sx, sy) __ mem:
            r.. mem[(sx, sy)]
        res = helper(sx, sx+sy, tx, ty, mem) o.\
            helper(sx+sy, sy, tx, ty, mem)
        mem[(sx, sy)] = res
        r.. res
    
    ___ test
        testCases = [
            [1, 1, 3, 5], # True
            [1, 1, 2, 2], # False
            [1, 1, 1, 1], # True
            [6, 5, 11, 16], # True
        ]
        ___ sx, sy, tx, ty __ testCases:
            print('sx: %s, sy: %s, tx: %s, ty: %s' % (sx, sy, tx, ty
            result = reachingPoints(sx, sy, tx, ty)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
