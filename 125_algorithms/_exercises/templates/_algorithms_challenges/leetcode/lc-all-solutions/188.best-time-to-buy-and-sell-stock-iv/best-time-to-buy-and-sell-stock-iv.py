______ heapq
______ random


class Solution(object
  ___ findKthLargest(self, nums, k
    """
    :type A: List[int]
    :type k: int
    :rtype: int
    """

    ___ quickselect(start, end, nums, k
      __ start __ end:
        r_ nums[start]

      mid = partition(start, end, nums)

      __ mid __ k:
        r_ nums[mid]
      ____ k > mid:
        r_ quickselect(mid + 1, end, nums, k)
      ____
        r_ quickselect(start, mid - 1, nums, k)

    ___ partition(start, end, nums
      p = random.randrange(start, end + 1)
      pv = nums[p]
      nums[end], nums[p] = nums[p], nums[end]
      mid = start
      for i in range(start, end
        __ nums[i] >= pv:
          nums[i], nums[mid] = nums[mid], nums[i]
          mid += 1
      nums[mid], nums[end] = nums[end], nums[mid]
      r_ mid

    r_ quickselect(0, le.(nums) - 1, nums, k - 1)

  ___ maxProfit(self, k, prices
    """
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    __ not prices:
      r_ 0
    stack = []
    heap = []
    v = p = 0
    n = le.(prices)
    ans = 0
    w___ p < n:
      v = p
      w___ v < n - 1 and prices[v] >= prices[v + 1]:
        v += 1
      p = v + 1
      w___ p < n and prices[p] > prices[p - 1]:
        p += 1
      w___ stack and prices[stack[-1][0]] > prices[v]:
        _v, _p = stack.pop()
        heap.append(prices[_p - 1] - prices[_v])
      w___ stack and prices[stack[-1][1] - 1] < prices[p - 1]:
        heap.append(prices[stack[-1][1] - 1] - prices[v])
        v, _ = stack.pop()
      stack.append((v, p))

    heap += [prices[p - 1] - prices[v] for v, p in stack]
    __ le.(heap) < k:
      r_ sum(heap)
    self.findKthLargest(heap, k)
    r_ sum(heap[:k])
