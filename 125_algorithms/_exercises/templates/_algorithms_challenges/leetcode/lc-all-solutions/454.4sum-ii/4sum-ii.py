c_ Solution(o..
  ___ fourSumCount  A, B, C, D
    """
    :type A: List[int]
    :type B: List[int]
    :type C: List[int]
    :type D: List[int]
    :rtype: int
    """
    ans = 0
    abDict    # dict
    ___ i __ r..(l..(A:
      ___ j __ r..(l..(B:
        __ A[i] + B[j] n.. __ abDict:
          abDict[A[i] + B[j]] = 1
        ____:
          abDict[A[i] + B[j]] += 1

    ___ i __ r..(l..(C:
      ___ j __ r..(l..(D:
        __ -C[i] - D[j] __ abDict:
          ans += abDict[-C[i] - D[j]]
    r.. ans
