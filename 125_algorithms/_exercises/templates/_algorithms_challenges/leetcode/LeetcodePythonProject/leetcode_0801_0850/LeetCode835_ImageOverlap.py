'''
Created on Jun 10, 2018

@author: tongq
'''
class Solution(object
    ___ largestOverlap(self, A, B
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        ______ collections
        n = le.(A)
        #encode the position of 1 in A and B
        #we can' t use i//n*n + i%n. Although it is a distinct way to encode position
        LA = [(i, j) for i in range(n) for j in range(n) __ A[i][j] __ 1]
        LB = [(i, j) for i in range(n) for j in range(n) __ B[i][j] __ 1]
        counts = collections.defaultdict(int)
        res = 0
        for i in LA:
            for j in LB:
                counts[(i[0]-j[0], i[1]-j[1])] += 1
                res = max(res, counts[(i[0]-j[0], i[1]-j[1])])
        r_ res
    
    ___ largestOverlap_another(self, A, B
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        n = le.(A)
        la = [i/n*100 + i%n for i in range(n*n) __ A[i/n][i%n]]
        lb = [i/n*100 + i%n for i in range(n*n) __ B[i/n][i%n]]
        count = {}
        for i in la:
            for j in lb:
                count[i-j] = count.get(i-j, 0)+1
        r_ max(count.values() or [0])
