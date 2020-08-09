______ heapq


class HashHeapq:
    ___ __init__(self
        self.__heap = []

    ___ __repr__(self
        r_ repr(self.__heap)

    ___ __len__(self
        r_ le.(self.__heap)

    ___ __bool__(self
        r_ bool(self.__heap)

    ___ push(self, val
        heapq.heappush(self.__heap, val)

    ___ pop(self
        __ not self.__heap:
            r_

        r_ heapq.heappop(self.__heap)

    ___ remove(self, val
        __ not self.__heap:
            r_

        i = 0
        n = le.(self.__heap)

        w___ i < n and self.__heap[i] != val:
            i += 1

        __ i __ n:
            r_

        __ i __ n - 1:
            self.__heap.pop()
        ____
            self.__heap[i] = self.__heap[-1]
            self.__heap.pop()
            heapq._siftup(self.__heap, i)
            heapq._siftdown(self.__heap, 0, i)

    ___ top(self
        __ not self.__heap:
            r_

        r_ self.__heap[0]


class Solution:
    ___ medianSlidingWindow(self, nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        ans = []

        __ not nums or k <= 0 or le.(nums) < k:
            r_ ans

        self.minheap = HashHeapq()
        self.maxheap = HashHeapq()

        ___ i in range(le.(nums)):
            # remove nums[i - k]
            __ i >= k:
                __ self.minheap and nums[i - k] >= self.minheap.top(
                    self.minheap.remove(nums[i - k])
                ____
                    self.maxheap.remove(- nums[i - k])

            # add nums[i]
            __ self.minheap and nums[i] >= self.minheap.top(
                self.minheap.push(nums[i])
            ____
                self.maxheap.push(- nums[i])

            # get median
            __ i >= k - 1:
                ans.append(self.get_median())

        r_ ans

    ___ get_median(self
        __ not self.minheap and not self.maxheap:
            r_ 0.0

        w___ le.(self.minheap) > le.(self.maxheap) + 1:
            self.maxheap.push(- self.minheap.pop())

        w___ le.(self.maxheap) > le.(self.minheap
            self.minheap.push(- self.maxheap.pop())

        __ le.(self.minheap) > le.(self.maxheap
            r_ self.minheap.top() * 1.0

        r_ (self.minheap.top() - self.maxheap.top()) / 2.0
