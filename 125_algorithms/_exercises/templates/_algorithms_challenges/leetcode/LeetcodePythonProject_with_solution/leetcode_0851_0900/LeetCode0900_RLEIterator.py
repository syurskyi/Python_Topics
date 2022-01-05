# Showing Memory Limit Exceeded only
# I hope it's OK

c_ RLEIterator(object):

    ___ - , A):
        """
        :type A: List[int]
        """
        arr = A
        countIdx = 0
        numIdx = 1

    ___ next  n):
        """
        :type n: int
        :rtype: int
        """
        val = -1
        ___ _ __ r..(n):
            w.... countIdx < l..(arr) a.. \
                    arr[countIdx] __ 0:
                countIdx += 2
                numIdx += 2
            __ countIdx >= l..(arr):
                r.. -1
            val = arr[numIdx]
            arr[countIdx] -= 1
        r.. val


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
