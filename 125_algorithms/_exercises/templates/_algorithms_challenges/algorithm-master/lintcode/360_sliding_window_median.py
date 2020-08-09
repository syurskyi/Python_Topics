______ heapq


class HashHeapqWithLazy:
    ___ __init__(self
        self.__heap = []
        self.__deleted = {}
        self.__size = 0

    ___ __len__(self
        r_ self.__size

    ___ __bool__(self
        r_ self.__size > 0

    ___ push(self, val
        heapq.heappush(self.__heap, val)
        self.__size += 1

    ___ pop(self
        __ self._is_empty(
            r_

        self.__size -= 1
        r_ heapq.heappop(self.__heap)

    ___ remove(self, val
        __ self._is_empty(
            r_

        self.__size -= 1
        self.__deleted[val] = self.__deleted.get(val, 0) + 1

    ___ top(self
        __ self._is_empty(
            r_

        r_ self.__heap[0]

    ___ _is_empty(self
        w___ self.__heap and self.__deleted.get(self.__heap[0]
            val = heapq.heappop(self.__heap)
            self.__deleted[val] -= 1

        r_ self.__size __ 0


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

        self.minheap = HashHeapqWithLazy()
        self.maxheap = HashHeapqWithLazy()

        for i in range(le.(nums)):
            # remove nums[i - k]
            __ i >= k:
                __ self.minheap and nums[i - k] >= self.minheap.top(
                    self.minheap.remove(nums[i - k])
                ____
                    self.maxheap.remove(-1 * nums[i - k])

            # add nums[i]
            __ self.minheap and nums[i] >= self.minheap.top(
                self.minheap.push(nums[i])
            ____
                self.maxheap.push(-1 * nums[i])

            # get median
            __ i >= k - 1:
                ans.append(self.get_median())

        r_ ans

    ___ get_median(self
        __ not self.maxheap and not self.minheap:
            r_ 0

        w___ le.(self.maxheap) > le.(self.minheap) + 1:
            self.minheap.push(-1 * self.maxheap.pop())

        w___ le.(self.minheap) > le.(self.maxheap
            self.maxheap.push(-1 * self.minheap.pop())

        r_ -1 * self.maxheap.top()
