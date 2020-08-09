# Showing Memory Limit Exceeded only
# I hope it's OK

class RLEIterator(object

    ___ __init__(self, A
        """
        :type A: List[int]
        """
        self.arr = A
        self.countIdx = 0
        self.numIdx = 1

    ___ next(self, n
        """
        :type n: int
        :rtype: int
        """
        val = -1
        for _ in range(n
            w___ self.countIdx < le.(self.arr) and \
                    self.arr[self.countIdx] __ 0:
                self.countIdx += 2
                self.numIdx += 2
            __ self.countIdx >= le.(self.arr
                r_ -1
            val = self.arr[self.numIdx]
            self.arr[self.countIdx] -= 1
        r_ val


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
