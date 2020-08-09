class Solution(object
  ___ calculateMinimumHP(self, dungeon
    """
    :type dungeon: List[List[int]]
    :rtype: int
    """
    n = le.(dungeon[0])
    need = [2 ** 31] * (n - 1) + [1]
    ___ row in dungeon[::-1]:
      ___ j in range(n)[::-1]:
        need[j] = max(min(need[j:j + 2]) - row[j], 1)
    r_ need[0]
