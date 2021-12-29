_______ heapq


class HashHeapqWithLazy:
    ___ __init__(self):
        self.__heap    # list
        self.__deleted = {}
        self.__size = 0

    ___ __len__(self):
        r.. self.__size

    ___ __bool__(self):
        r.. self.__size > 0

    ___ push(self, val):
        heapq.heappush(self.__heap, val)
        self.__size += 1

    ___ pop(self):
        __ self._is_empty():
            r..

        self.__size -= 1
        r.. heapq.heappop(self.__heap)

    ___ remove(self, val):
        __ self._is_empty():
            r..

        self.__size -= 1
        self.__deleted[val] = self.__deleted.get(val, 0) + 1

    ___ top(self):
        __ self._is_empty():
            r..

        r.. self.__heap[0]

    ___ _is_empty(self):
        w.... self.__heap a.. self.__deleted.get(self.__heap[0]):
            val = heapq.heappop(self.__heap)
            self.__deleted[val] -= 1

        r.. self.__size __ 0


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

        self.minheap = HashHeapqWithLazy()
        self.maxheap = HashHeapqWithLazy()

        ___ i __ r..(l..(nums)):
            # remove nums[i - k]
            __ i >= k:
                __ self.minheap a.. nums[i - k] >= self.minheap.top():
                    self.minheap.remove(nums[i - k])
                ____:
                    self.maxheap.remove(-1 * nums[i - k])

            # add nums[i]
            __ self.minheap a.. nums[i] >= self.minheap.top():
                self.minheap.push(nums[i])
            ____:
                self.maxheap.push(-1 * nums[i])

            # get median
            __ i >= k - 1:
                ans.a..(self.get_median())

        r.. ans

    ___ get_median(self):
        __ n.. self.maxheap a.. n.. self.minheap:
            r.. 0

        w.... l..(self.maxheap) > l..(self.minheap) + 1:
            self.minheap.push(-1 * self.maxheap.pop())

        w.... l..(self.minheap) > l..(self.maxheap):
            self.maxheap.push(-1 * self.minheap.pop())

        r.. -1 * self.maxheap.top()
