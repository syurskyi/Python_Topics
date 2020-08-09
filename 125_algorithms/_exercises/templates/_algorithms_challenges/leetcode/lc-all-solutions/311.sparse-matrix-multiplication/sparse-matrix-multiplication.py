class Solution(object
  ___ multiply(self, A, B
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    ret = [[0 ___ j in range(le.(B[0]))] ___ i in range(le.(A))]

    ___ i, row in enumerate(A
      ___ k, a in enumerate(row
        __ a:
          ___ j, b in enumerate(B[k]
            __ b:
              ret[i][j] += a * b
    r_ ret
