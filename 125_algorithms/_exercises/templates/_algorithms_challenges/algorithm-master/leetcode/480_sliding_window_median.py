_______ heapq


class HashHeapq:
    ___ __init__(self):
        self.__heap    # list

    ___ __repr__(self):
        r.. repr(self.__heap)

    ___ __len__(self):
        r.. l..(self.__heap)

    ___ __bool__(self):
        r.. bool(self.__heap)

    ___ push(self, val):
        heapq.heappush(self.__heap, val)

    ___ pop(self):
        __ n.. self.__heap:
            r..

        r.. heapq.heappop(self.__heap)

    ___ remove(self, val):
        __ n.. self.__heap:
            r..

        i = 0
        n = l..(self.__heap)

        w.... i < n a.. self.__heap[i] != val:
            i += 1

        __ i __ n:
            r..

        __ i __ n - 1:
            self.__heap.pop()
        ____:
            self.__heap[i] = self.__heap[-1]
            self.__heap.pop()
            heapq._siftup(self.__heap, i)
            heapq._siftdown(self.__heap, 0, i)

    ___ top(self):
        __ n.. self.__heap:
            r..

        r.. self.__heap[0]


class Solution:
    ___ medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        ans    # list

        __ n.. nums o. k <= 0 o. l..(nums) < k:
            r.. ans

        self.minheap = HashHeapq()
        self.maxheap = HashHeapq()

        ___ i __ r..(l..(nums)):
            # remove nums[i - k]
            __ i >= k:
                __ self.minheap a.. nums[i - k] >= self.minheap.top():
                    self.minheap.remove(nums[i - k])
                ____:
                    self.maxheap.remove(- nums[i - k])

            # add nums[i]
            __ self.minheap a.. nums[i] >= self.minheap.top():
                self.minheap.push(nums[i])
            ____:
                self.maxheap.push(- nums[i])

            # get median
            __ i >= k - 1:
                ans.a..(self.get_median())

        r.. ans

    ___ get_median(self):
        __ n.. self.minheap a.. n.. self.maxheap:
            r.. 0.0

        w.... l..(self.minheap) > l..(self.maxheap) + 1:
            self.maxheap.push(- self.minheap.pop())

        w.... l..(self.maxheap) > l..(self.minheap):
            self.minheap.push(- self.maxheap.pop())

        __ l..(self.minheap) > l..(self.maxheap):
            r.. self.minheap.top() * 1.0

        r.. (self.minheap.top() - self.maxheap.top()) / 2.0
