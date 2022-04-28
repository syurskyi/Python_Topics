c_ LRUCache o..
    ___ -  capacity):
        """
        :type capacity: int
        """
        capacity = capacity
        cache  # dict
        queue = []

    ___ updateQueue  key):
        queue.remove(key)
        queue.insert(0, key)

    ___ get  key):
        """
        :rtype: int
        """
        __ key __ cache:
            updateQueue(key)
            r_ cache[key]
        ____
            r_ -1

    ___ put  key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        __ key __ cache:
            queue.remove(key)
        ____ l.. queue) __ capacity:
            del cache[queue.pop(-1)]

        cache[key] = value
        queue.insert(0, key)

    # def __init__(self, capacity):
    #     self.dic = collections.OrderedDict()
    #     self.remain = capacity
    #
    # def get(self, key):
    #     if key not in self.dic:
    #         return -1
    #     v = self.dic.pop(key)
    #     self.dic[key] = v  # set key as the newest one
    #     return v
    #
    # def put(self, key, value):
    #     if key in self.dic:
    #         self.dic.pop(key)
    #     else:
    #         if self.remain > 0:
    #             self.remain -= 1
    #         else:  # self.dic is full
    #             self.dic.popitem(last=False)
    #     self.dic[key] = value