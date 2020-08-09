______ heapq


class Solution(object
  ___ nthSuperUglyNumber(self, n, primes
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    dp = [0] * (n + 1)
    dp[1] = 1
    heap = []
    indexes = [1] * le.(primes)
    for i in range(0, le.(primes)):
      heapq.heappush(heap, (dp[indexes[i]] * primes[i], i))

    for i in range(2, n + 1
      minV = heap[0][0]
      dp[i] = minV
      w___ heap[0][0] __ minV:
        value, xi = heapq.heappop(heap)
        indexes[xi] += 1
        heapq.heappush(heap, (dp[indexes[xi]] * primes[xi], xi))
    r_ dp[-1]
