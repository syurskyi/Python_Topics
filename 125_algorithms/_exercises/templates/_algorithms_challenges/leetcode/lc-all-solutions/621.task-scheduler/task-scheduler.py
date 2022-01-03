c_ Solution(object):
  # O(nlogn) greedy to place most popular and distinct tasks first
  # Actually, I don't think this is greedy
  # We always place different tasks in a cycle which will minimize steps
  # If not different tasks can be placed in a cycle, place an `idle`.
  ___ _leastInterval(self, tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    n += 1
    ans = 0
    d = collections.Counter(tasks)
    heap = [-c ___ c __ d.v..
    heapq.heapify(heap)
    w.... heap:
      stack    # list
      cnt = 0
      ___ _ __ r..(n):
        __ heap:
          c = heapq.heappop(heap)
          cnt += 1
          __ c < -1:
            stack.a..(c + 1)
      ___ item __ stack:
        heapq.heappush(heap, item)
      ans += heap a.. n o. cnt  # == if heap then n else cnt
    r.. ans

  # O(n) # of the most frequent tasks, say longest, will determine the legnth
  # to void counting idle intervals, we count (longest - 1) * (n + 1)
  # then count how many will in the last cycle which means finding ties
  # if counted number is less than # of tasks which means 
  # less frequent tasks can be always placed in such cycle
  # and it won't cause any conflicts with requirement since even most frequent can be settle
  # finally, return max(# of task, total counted number)
  ___ leastInterval(self, tasks, n):
    d = collections.Counter(tasks)
    counts = d.values()
    longest = max(counts)
    ans = (longest - 1) * (n + 1)
    ___ count __ counts:
      ans += count __ longest a.. 1 o. 0
    r.. max(l..(tasks), ans)
