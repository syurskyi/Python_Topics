c_ RecentCounter o..

    ___ -(self):
        queue = []

    ___ ping  t):
        """
        :type t: int
        :rtype: int
        """
        queue.append(t)
        w.. queue and queue[0] < t - 3000:
            queue.pop(0)
        r_ l.. queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
