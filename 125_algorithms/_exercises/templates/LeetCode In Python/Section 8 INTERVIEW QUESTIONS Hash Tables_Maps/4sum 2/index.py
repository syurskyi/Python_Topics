c_ Solution:
    ___ fourSumCount(, A: L.. in., B: L.. in., C: L.. in., D: L.. in.) -> in.:
      m _ {}
      ans _ 0

      ___ i __ ra..(0,le.(A)):
        x _ A[i]
        ___ j __ ra..(0,le.(B)):
          y _ B[j]
          __(x+y no. __ m
            m[x+y] _ 0
          m[x+y]+_1

      ___ i __ ra..(0,le.(C)):
        x _ C[i]
        ___ j __ ra..(0,le.(D)):
          y _ D[j]
          target _ -(x+y)
          __(target __ m
            ans+_m[target]

      r_ ans