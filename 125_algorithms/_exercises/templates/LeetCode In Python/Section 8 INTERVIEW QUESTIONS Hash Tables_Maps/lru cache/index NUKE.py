____ collections _______ deque


class LRUCache:

    ___ __init__(self, capacity: i..):
        self.c  capacity
        self.m  d..()
        self.deq  deque()

    ___ get(self, key: i..) -> i..:
        __ key __ self.m:
            value  self.m[key]
            self.deq.remove(key)
            self.deq.a..(key)
            r.. value
        ____:
            r.. -1

    ___ put(self, key: i.., value: i..) -> N..:

        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)
        __ key n.. __ self.m:
            __ l..(self.deq) __ self.c:
                oldest  self.deq.popleft()
                del self.m[oldest]
        ____:
            self.deq.remove(key)

        self.m[key]  value
        self.deq.a..(key)
