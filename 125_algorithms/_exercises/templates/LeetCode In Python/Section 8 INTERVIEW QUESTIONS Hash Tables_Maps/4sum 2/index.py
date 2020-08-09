class Solution:
    ___ fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
      m = {}
      ans = 0

      ___ i __ ra..(0,le.(A)):
        x = A[i]
        ___ j __ ra..(0,le.(B)):
          y = B[j]
          __(x+y not __ m
            m[x+y] = 0
          m[x+y]+=1

      ___ i __ ra..(0,le.(C)):
        x = C[i]
        ___ j __ ra..(0,le.(D)):
          y = D[j]
          target = -(x+y)
          __(target __ m
            ans+=m[target]

      r_ ans