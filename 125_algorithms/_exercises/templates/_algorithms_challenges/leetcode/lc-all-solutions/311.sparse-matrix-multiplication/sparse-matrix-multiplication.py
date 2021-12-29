class Solution(object):
  ___ multiply(self, A, B):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    ret = [[0 for j in range(len(B[0]))] for i in range(len(A))]

    for i, row in enumerate(A):
      for k, a in enumerate(row):
        __ a:
          for j, b in enumerate(B[k]):
            __ b:
              ret[i][j] += a * b
    return ret
