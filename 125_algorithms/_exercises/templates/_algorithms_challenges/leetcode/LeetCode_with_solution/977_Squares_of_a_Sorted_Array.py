c_ Solution o..
    # def sortedSquares(self, A):
    #     """
    #     :type A: List[int]
    #     :rtype: List[int]
    #     """
    #     # Directly sort
    #     return sorted(x * x for x in A) 

    ___ sortedSquares  A):
        pos = 0
        w.. pos < l.. A) and A[pos] < 0:
            pos += 1
        # pos point to first positve
        # npos point to larget negative
        npos = pos - 1
        res =    # list
        w.. pos < l.. A) and npos >= 0:
            __ A[npos] ** 2 < A[pos] ** 2:
                res.append(A[npos] ** 2)
                npos -= 1
            ____
                res.append(A[pos] ** 2)
                pos +=1 
        w.. npos >= 0:
            res.append(A[npos] ** 2)
            npos -= 1
        w.. pos < l.. A):
            res.append(A[pos] ** 2)
            pos += 1
        r_ res
