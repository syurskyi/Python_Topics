'''
Created on Jun 10, 2018

@author: tongq
'''
c_ Solution(o..):
    ___ largestOverlap  A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        _______ c..
        n = l..(A)
        #encode the position of 1 in A and B
        #we can' t use i//n*n + i%n. Although it is a distinct way to encode position
        LA = [(i, j) ___ i __ r..(n) ___ j __ r..(n) __ A[i][j] __ 1]
        LB = [(i, j) ___ i __ r..(n) ___ j __ r..(n) __ B[i][j] __ 1]
        counts = c...defaultdict(i..)
        res = 0
        ___ i __ LA:
            ___ j __ LB:
                counts[(i[0]-j[0], i[1]-j[1])] += 1
                res = m..(res, counts[(i[0]-j[0], i[1]-j[1])])
        r.. res
    
    ___ largestOverlap_another  A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        n = l..(A)
        la = [i/n*100 + i%n ___ i __ r..(n*n) __ A[i/n][i%n]]
        lb = [i/n*100 + i%n ___ i __ r..(n*n) __ B[i/n][i%n]]
        count    # dict
        ___ i __ la:
            ___ j __ lb:
                count[i-j] = count.get(i-j, 0)+1
        r.. m..(count.v.. o. [0])
