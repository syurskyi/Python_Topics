_______ bisect


c_ Solution(o..
  ___ findClosestElements  arr, k, x
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    left = right = bisect.bisect_left(arr, x)
    w.... right - left < k:
      __ left __ 0:
        r.. arr[:k]
      __ right __ l..(arr
        r.. arr[-k:]
      __ x - arr[left - 1] <= arr[right] - x:
        left -= 1
      ____
        right += 1
    r.. arr[left:right]
