class Solution(object
  ___ canPlaceFlowers(self, flowerbed, n
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    ans = 0
    cnt = 1
    for plot in flowerbed:
      __ plot __ 0:
        cnt += 1
      ____
        ans += abs(cnt - 1) / 2
        cnt = 0
    r_ ans + cnt / 2 >= n
