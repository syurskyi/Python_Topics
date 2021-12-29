import heapq


class HashHeapqWithLazy:
    ___ __init__(self):
        self.__heap = []
        self.__deleted = {}
        self.__size = 0

    ___ __len__(self):
        return self.__size

    ___ __bool__(self):
        return self.__size > 0

    ___ push(self, val):
        heapq.heappush(self.__heap, val)
        self.__size += 1

    ___ pop(self):
        __ self._is_empty():
            return

        self.__size -= 1
        return heapq.heappop(self.__heap)

    ___ remove(self, val):
        __ self._is_empty():
            return

        self.__size -= 1
        self.__deleted[val] = self.__deleted.get(val, 0) + 1

    ___ top(self):
        __ self._is_empty():
            return

        return self.__heap[0]

    ___ _is_empty(self):
        while self.__heap and self.__deleted.get(self.__heap[0]):
            val = heapq.heappop(self.__heap)
            self.__deleted[val] -= 1

        return self.__size == 0


class Solution:
    ___ medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        ans = []

        __ not nums or k <= 0 or len(nums) < k:
            return ans

        self.minheap = HashHeapqWithLazy()
        self.maxheap = HashHeapqWithLazy()

        for i in range(len(nums)):
            # remove nums[i - k]
            __ i >= k:
                __ self.minheap and nums[i - k] >= self.minheap.top():
                    self.minheap.remove(nums[i - k])
                else:
                    self.maxheap.remove(-1 * nums[i - k])

            # add nums[i]
            __ self.minheap and nums[i] >= self.minheap.top():
                self.minheap.push(nums[i])
            else:
                self.maxheap.push(-1 * nums[i])

            # get median
            __ i >= k - 1:
                ans.append(self.get_median())

        return ans

    ___ get_median(self):
        __ not self.maxheap and not self.minheap:
            return 0

        while len(self.maxheap) > len(self.minheap) + 1:
            self.minheap.push(-1 * self.maxheap.pop())

        while len(self.minheap) > len(self.maxheap):
            self.maxheap.push(-1 * self.minheap.pop())

        return -1 * self.maxheap.top()
