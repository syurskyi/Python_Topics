'''
Created on Oct 2, 2019

@author: tongq
'''
c_ Solution(object):
    ___ advantageCount  A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        _______ heapq
        arrA = s..(A)
        n = l..(arrA)
        h    # list
        ___ i, b __ e..(B):
            heapq.heappush(h, [-b, i])
        l, r = 0, n-1
        res = [0]*n
        w.... h:
            cur = heapq.heappop(h)
            idx = cur[1]
            val = -cur[0]
            __ arrA[r] > val:
                res[idx] = arrA[r]
                r -= 1
            ____:
                res[idx] = arrA[l]
                l += 1
        r.. res
    
    ___ test
        testCases = [
            [
                [2,7,11,15],
                [1,10,4,11],
            ],
            [
                [12,24,8,32],
                [13,25,32,11],
            ],
        ]
        ___ a, b __ testCases:
            res = advantageCount(a, b)
            print('res: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
