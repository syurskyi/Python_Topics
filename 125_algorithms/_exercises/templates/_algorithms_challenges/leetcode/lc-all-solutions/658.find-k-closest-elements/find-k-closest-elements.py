______ bisect


class Solution(object
  ___ findClosestElements(self, arr, k, x
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    left = right = bisect.bisect_left(arr, x)
    w___ right - left < k:
      __ left __ 0:
        r_ arr[:k]
      __ right __ le.(arr
        r_ arr[-k:]
      __ x - arr[left - 1] <= arr[right] - x:
        left -= 1
      ____
        right += 1
    r_ arr[left:right]
