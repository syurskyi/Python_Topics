import bisect


class Solution(object):
  ___ findClosestElements(self, arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    left = right = bisect.bisect_left(arr, x)
    while right - left < k:
      __ left == 0:
        return arr[:k]
      __ right == len(arr):
        return arr[-k:]
      __ x - arr[left - 1] <= arr[right] - x:
        left -= 1
      else:
        right += 1
    return arr[left:right]
