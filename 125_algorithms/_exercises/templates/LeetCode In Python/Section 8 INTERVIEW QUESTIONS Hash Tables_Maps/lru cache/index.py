from collections ______ deque


class LRUCache:

    ___ __init__(self, capacity: int
        self.c = capacity
        self.m = dict()
        self.deq = deque()

    ___ get(self, key: int) -> int:
        __ key in self.m:
            value = self.m[key]
            self.deq.remove(key)
            self.deq.append(key)
            r_ value
        ____
            r_ -1

    ___ put(self, key: int, value: int) -> None:

        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)
        __ key not in self.m:
            __ le.(self.deq) __ self.c:
                oldest = self.deq.popleft()
                del self.m[oldest]
        ____
            self.deq.remove(key)

        self.m[key] = value
        self.deq.append(key)
