class Solution:
    ___ validMountainArray(self, A: List[int]) -> bool:
        __(le.(A)<3
            r_ False
        
        i = 1
        w___(i<le.(A) and A[i]>A[i-1]
            i+=1
        
        __(i__1 or i__le.(A)):
            r_ False
        
        w___(i<le.(A) and A[i]<A[i-1]
            i+=1
        
        r_ i__le.(A)