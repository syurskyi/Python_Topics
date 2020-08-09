c_ Solution:
    ___ validMountainArray(, A: L.. in.) -> bool:
        __(le.(A)<3
            r_ False
        
        i _ 1
        w___(i<le.(A) and A[i]>A[i-1]
            i+_1
        
        __(i__1 or i__le.(A)):
            r_ False
        
        w___(i<le.(A) and A[i]<A[i-1]
            i+_1
        
        r_ i__le.(A)