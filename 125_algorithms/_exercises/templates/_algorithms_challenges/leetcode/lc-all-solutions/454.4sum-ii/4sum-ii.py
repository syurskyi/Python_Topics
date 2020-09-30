class Solution(object
  ___ fourSumCount(self, A, B, C, D
    """
    :type A: List[int]
    :type B: List[int]
    :type C: List[int]
    :type D: List[int]
    :rtype: int
    """
    ans = 0
    abDict = {}
    ___ i __ range(le.(A)):
      ___ j __ range(le.(B)):
        __ A[i] + B[j] not __ abDict:
          abDict[A[i] + B[j]] = 1
        ____
          abDict[A[i] + B[j]] += 1

    ___ i __ range(le.(C)):
      ___ j __ range(le.(D)):
        __ -C[i] - D[j] __ abDict:
          ans += abDict[-C[i] - D[j]]
    r_ ans
