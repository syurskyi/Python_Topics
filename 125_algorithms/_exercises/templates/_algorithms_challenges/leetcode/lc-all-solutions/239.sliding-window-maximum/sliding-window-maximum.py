c_ Solution(o..):
  ___ maxSlidingWindow  nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    __ k __ 0:
      r.. []
    ans = [0 ___ _ __ r..(l..(nums) - k + 1)]
    stack = c...d..([])
    ___ i __ r..(0, k):
      w.... stack a.. nums[stack[-1]] < nums[i]:
        stack.pop()
      stack.a..(i)
    ans[0] = nums[stack[0]]
    idx = 0
    ___ i __ r..(k, l..(nums)):
      idx += 1
      __ stack a.. stack[0] __ i - k:
        stack.popleft()
      w.... stack a.. nums[stack[-1]] < nums[i]:
        stack.pop()
      stack.a..(i)
      ans[idx] = nums[stack[0]]

    r.. ans
