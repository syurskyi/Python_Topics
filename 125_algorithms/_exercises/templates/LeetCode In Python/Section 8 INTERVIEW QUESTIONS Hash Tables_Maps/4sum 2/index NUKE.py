c_ Solution:
    ___ fourSumCount(self, A: List[i..], B: List[i..], C: List[i..], D: List[i..]) __ i..:
      m  {}
      ans  0

      ___ i __ r..(0,l..(A)):
        x  A[i]
        ___ j __ r..(0,l..(B)):
          y  B[j]
          __(x+y n.. __ m):
            m[x+y]  0
          m[x+y]+1

      ___ i __ r..(0,l..(C)):
        x  C[i]
        ___ j __ r..(0,l..(D)):
          y  D[j]
          target  -(x+y)
          __(target __ m):
            ans+m[target]

      r.. ans