from collections import deque


class LRUCache:

    def __init__(self, capacity: i..):
        self.c  capacity
        self.m  dict()
        self.deq  deque()

    def get(self, key: i..) -> i..:
        __ key in self.m:
            value  self.m[key]
            self.deq.remove(key)
            self.deq.append(key)
            return value
        else:
            return -1

    def put(self, key: i.., value: i..) -> N..:

        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)
        __ key not in self.m:
            __ len(self.deq) __ self.c:
                oldest  self.deq.popleft()
                del self.m[oldest]
        else:
            self.deq.remove(key)

        self.m[key]  value
        self.deq.append(key)
