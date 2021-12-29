_______ heapq
_______ random


class Solution(object):
  ___ findKthLargest(self, nums, k):
    """
    :type A: List[int]
    :type k: int
    :rtype: int
    """

    ___ quickselect(start, end, nums, k):
      __ start __ end:
        r.. nums[start]

      mid = partition(start, end, nums)

      __ mid __ k:
        r.. nums[mid]
      ____ k > mid:
        r.. quickselect(mid + 1, end, nums, k)
      ____:
        r.. quickselect(start, mid - 1, nums, k)

    ___ partition(start, end, nums):
      p = random.randrange(start, end + 1)
      pv = nums[p]
      nums[end], nums[p] = nums[p], nums[end]
      mid = start
      ___ i __ r..(start, end):
        __ nums[i] >= pv:
          nums[i], nums[mid] = nums[mid], nums[i]
          mid += 1
      nums[mid], nums[end] = nums[end], nums[mid]
      r.. mid

    r.. quickselect(0, l..(nums) - 1, nums, k - 1)

  ___ maxProfit(self, k, prices):
    """
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    __ n.. prices:
      r.. 0
    stack    # list
    heap    # list
    v = p = 0
    n = l..(prices)
    ans = 0
    w.... p < n:
      v = p
      w.... v < n - 1 a.. prices[v] >= prices[v + 1]:
        v += 1
      p = v + 1
      w.... p < n a.. prices[p] > prices[p - 1]:
        p += 1
      w.... stack a.. prices[stack[-1][0]] > prices[v]:
        _v, _p = stack.pop()
        heap.a..(prices[_p - 1] - prices[_v])
      w.... stack a.. prices[stack[-1][1] - 1] < prices[p - 1]:
        heap.a..(prices[stack[-1][1] - 1] - prices[v])
        v, _ = stack.pop()
      stack.a..((v, p))

    heap += [prices[p - 1] - prices[v] ___ v, p __ stack]
    __ l..(heap) < k:
      r.. s..(heap)
    self.findKthLargest(heap, k)
    r.. s..(heap[:k])
