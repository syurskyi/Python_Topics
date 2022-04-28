c_ Solution o..
#     def topKFrequent(self, words, k):
#         """
#         :type words: List[str]
#         :type k: int
#         :rtype: List[str]
#         """
#         counter = collections.Counter(words)
#         res = sorted(counter.items(), cmp=cmp_frequency, reverse=True)
#         return [k for k, _ in res[:k]]

# def cmp_frequency(x, y):
#     if x[1] != y[1]:
#         return cmp(x[1], y[1])
#     return cmp(y[0], x[0])

    # def topKFrequent(self, words, k):
    #     count = collections.Counter(words)
    #     candidates = count.keys()
    #     candidates.sort(key = lambda w: (-count[w], w))
    #     return candidates[:k]

    ___ topKFrequent  words, k):
        count = collections.Counter(words)
        # Note that python heapq only support min heap
        # So, we can make the value negative to create a max heap
        heap = [(-freq, word) ___ word, freq __ count.items()]
        heapq.heapify(heap)
        r_ [heapq.heappop(heap)[1] ___ _ __ xrange(k)]
