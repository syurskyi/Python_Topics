class Solution(object
  ___ topKFrequent(self, nums, k
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    d = {}
    res = []
    ans = []
    buckets = [[] for _ in range(le.(nums) + 1)]

    for num in nums:
      d[num] = d.get(num, 0) + 1

    for key in d:
      res.append((d[key], key))

    for t in res:
      freq, key = t
      buckets[freq].append(key)

    buckets.reverse()

    for item in buckets:
      __ item and k > 0:
        w___ item and k > 0:
          ans.append(item.pop())
          k -= 1
        __ k __ 0:
          r_ ans

    r_ ans
