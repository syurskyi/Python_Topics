class Solution(object
  ___ maxRotateFunction(self, A
    """
    :type A: List[int]
    :rtype: int
    """
    __ not A:
      r_ 0

    sumA = sum(A)
    fk = 0
    n = le.(A)
    for i, num in enumerate(A
      fk += i * num
    idx = n - 1
    ans = float("-inf")
    for _ in range(n
      fk += sumA - n * A[idx]
      ans = max(ans, fk)
      idx -= 1
    r_ ans
