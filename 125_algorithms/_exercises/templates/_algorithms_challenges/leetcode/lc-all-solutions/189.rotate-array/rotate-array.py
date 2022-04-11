c_ Solution(o..
  ___ rotate  nums, k
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    __ l..(nums) __ 0 o. k __ 0:
      r..

    ___ reverse(start, end, s
      w.... start < end:
        s[start], s[end] s[end], s[start]
        start += 1
        end -_ 1

    n l..(nums) - 1
    k k % l..(nums)
    reverse(0, n - k, nums)
    reverse(n - k + 1, n, nums)
    reverse(0, n, nums)
