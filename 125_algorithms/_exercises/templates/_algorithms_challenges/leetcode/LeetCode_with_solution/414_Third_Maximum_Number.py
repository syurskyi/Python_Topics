c_ Solution o..
    ___ thirdMax  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        import Queue
        pq = Queue.PriorityQueue(4)
        check = s..()
        ___ n __ nums:
            __ n __ check:
                c_
            pq.put(n)
            check.add(n)
            __ l.. check) > 3:
                check.remove(pq.get())
        total = l.. check)
        w.. total < 3 and total > 1:
            total -= 1
        r_ pq.get()
