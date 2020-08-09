class Solution:
    ___ fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
      m = {}
      ans = 0

      for i in range(0,le.(A)):
        x = A[i]
        for j in range(0,le.(B)):
          y = B[j]
          __(x+y not in m
            m[x+y] = 0
          m[x+y]+=1

      for i in range(0,le.(C)):
        x = C[i]
        for j in range(0,le.(D)):
          y = D[j]
          target = -(x+y)
          __(target in m
            ans+=m[target]

      r_ ans