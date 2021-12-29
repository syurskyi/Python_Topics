class Solution:
    def fourSumCount(self, A: List[i..], B: List[i..], C: List[i..], D: List[i..]) -> i..:
      m  {}
      ans  0

      for i in range(0,len(A)):
        x  A[i]
        for j in range(0,len(B)):
          y  B[j]
          __(x+y not in m):
            m[x+y]  0
          m[x+y]+1

      for i in range(0,len(C)):
        x  C[i]
        for j in range(0,len(D)):
          y  D[j]
          target  -(x+y)
          __(target in m):
            ans+m[target]

      return ans