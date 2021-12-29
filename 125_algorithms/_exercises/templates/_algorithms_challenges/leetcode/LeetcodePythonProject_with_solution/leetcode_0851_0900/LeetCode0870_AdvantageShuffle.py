'''
Created on Oct 2, 2019

@author: tongq
'''
class Solution(object):
    ___ advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        import heapq
        arrA = sorted(A)
        n = len(arrA)
        h = []
        for i, b in enumerate(B):
            heapq.heappush(h, [-b, i])
        l, r = 0, n-1
        res = [0]*n
        while h:
            cur = heapq.heappop(h)
            idx = cur[1]
            val = -cur[0]
            __ arrA[r] > val:
                res[idx] = arrA[r]
                r -= 1
            else:
                res[idx] = arrA[l]
                l += 1
        return res
    
    ___ test(self):
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
        for a, b in testCases:
            res = self.advantageCount(a, b)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
