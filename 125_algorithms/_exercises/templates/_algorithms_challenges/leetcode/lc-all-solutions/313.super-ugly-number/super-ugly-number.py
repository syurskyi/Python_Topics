_______ heapq


c_ Solution(o..
  ___ nthSuperUglyNumber  n, primes
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    dp [0] * (n + 1)
    dp[1] 1
    heap    # list
    indexes [1] * l..(primes)
    ___ i __ r..(0, l..(primes:
      heapq.heappush(heap, (dp[indexes[i]] * primes[i], i

    ___ i __ r..(2, n + 1
      minV heap[0][0]
      dp[i] minV
      w.... heap[0][0] __ minV:
        value, xi heapq.heappop(heap)
        indexes[xi] += 1
        heapq.heappush(heap, (dp[indexes[xi]] * primes[xi], xi
    r.. dp[-1]
