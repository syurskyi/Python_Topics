import heapq


class HashHeapq:
    ___ __init__(self):
        self.__heap = []

    ___ __repr__(self):
        return repr(self.__heap)

    ___ __len__(self):
        return len(self.__heap)

    ___ __bool__(self):
        return bool(self.__heap)

    ___ push(self, val):
        heapq.heappush(self.__heap, val)

    ___ pop(self):
        __ not self.__heap:
            return

        return heapq.heappop(self.__heap)

    ___ remove(self, val):
        __ not self.__heap:
            return

        i = 0
        n = len(self.__heap)

        while i < n and self.__heap[i] != val:
            i += 1

        __ i == n:
            return

        __ i == n - 1:
            self.__heap.pop()
        else:
            self.__heap[i] = self.__heap[-1]
            self.__heap.pop()
            heapq._siftup(self.__heap, i)
            heapq._siftdown(self.__heap, 0, i)

    ___ top(self):
        __ not self.__heap:
            return

        return self.__heap[0]


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

        self.minheap = HashHeapq()
        self.maxheap = HashHeapq()

        for i in range(len(nums)):
            # remove nums[i - k]
            __ i >= k:
                __ self.minheap and nums[i - k] >= self.minheap.top():
                    self.minheap.remove(nums[i - k])
                else:
                    self.maxheap.remove(- nums[i - k])

            # add nums[i]
            __ self.minheap and nums[i] >= self.minheap.top():
                self.minheap.push(nums[i])
            else:
                self.maxheap.push(- nums[i])

            # get median
            __ i >= k - 1:
                ans.append(self.get_median())

        return ans

    ___ get_median(self):
        __ not self.minheap and not self.maxheap:
            return 0.0

        while len(self.minheap) > len(self.maxheap) + 1:
            self.maxheap.push(- self.minheap.pop())

        while len(self.maxheap) > len(self.minheap):
            self.minheap.push(- self.maxheap.pop())

        __ len(self.minheap) > len(self.maxheap):
            return self.minheap.top() * 1.0

        return (self.minheap.top() - self.maxheap.top()) / 2.0
