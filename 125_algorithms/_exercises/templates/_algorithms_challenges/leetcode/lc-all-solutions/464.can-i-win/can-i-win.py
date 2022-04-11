c_ Solution(o..
  ___ canIWin  maxChoosableInteger, desiredTotal
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """

    ___ helper(pool, target, visited
      __ pool __ visited:
        r.. visited[pool]
      __ target <_ 0:
        r.. F..
      __ pool >_ maxPool:
        r.. T..

      mask 0x01
      ___ i __ r..(0, maxChoosableInteger
        __ pool & mask __ 0:
          newPool pool | mask
          __ helper(newPool, target - (i + 1), visited) __ F..:
            visited[pool] T..
            r.. T..
        mask mask << 1
      visited[pool] F..
      r.. F..

    __ (1 + maxChoosableInteger) * (maxChoosableInteger / 2) < desiredTotal:
      r.. F..

    __ desiredTotal __ 0:
      r.. T..
    maxPool 0
    mask 1
    ___ i __ r..(0, maxChoosableInteger
      maxPool |= mask
      mask mask << 1
    pool 0
    visited    # dict
    r.. helper(pool, desiredTotal, visited)
