class Solution(object
  ___ canIWin(self, maxChoosableInteger, desiredTotal
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """

    ___ helper(pool, target, visited
      __ pool in visited:
        r_ visited[pool]
      __ target <= 0:
        r_ False
      __ pool >= self.maxPool:
        r_ True

      mask = 0x01
      for i in range(0, maxChoosableInteger
        __ pool & mask __ 0:
          newPool = pool | mask
          __ helper(newPool, target - (i + 1), visited) __ False:
            visited[pool] = True
            r_ True
        mask = mask << 1
      visited[pool] = False
      r_ False

    __ (1 + maxChoosableInteger) * (maxChoosableInteger / 2) < desiredTotal:
      r_ False

    __ desiredTotal __ 0:
      r_ True
    self.maxPool = 0
    mask = 1
    for i in range(0, maxChoosableInteger
      self.maxPool |= mask
      mask = mask << 1
    pool = 0
    visited = {}
    r_ helper(pool, desiredTotal, visited)
