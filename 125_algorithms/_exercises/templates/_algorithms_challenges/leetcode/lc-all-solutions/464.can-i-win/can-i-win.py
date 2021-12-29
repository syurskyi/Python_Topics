class Solution(object):
  ___ canIWin(self, maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """

    ___ helper(pool, target, visited):
      __ pool __ visited:
        r.. visited[pool]
      __ target <= 0:
        r.. False
      __ pool >= self.maxPool:
        r.. True

      mask = 0x01
      ___ i __ r..(0, maxChoosableInteger):
        __ pool & mask __ 0:
          newPool = pool | mask
          __ helper(newPool, target - (i + 1), visited) __ False:
            visited[pool] = True
            r.. True
        mask = mask << 1
      visited[pool] = False
      r.. False

    __ (1 + maxChoosableInteger) * (maxChoosableInteger / 2) < desiredTotal:
      r.. False

    __ desiredTotal __ 0:
      r.. True
    self.maxPool = 0
    mask = 1
    ___ i __ r..(0, maxChoosableInteger):
      self.maxPool |= mask
      mask = mask << 1
    pool = 0
    visited = {}
    r.. helper(pool, desiredTotal, visited)
