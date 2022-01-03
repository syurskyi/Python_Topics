____ collections _______ deque


c_ LRUCache:

    ___ - , capacity: i..):
        c  capacity
        m  d..()
        deq  deque()

    ___ get(self, key: i..) -> i..:
        __ key __ m:
            value  m[key]
            deq.remove(key)
            deq.a..(key)
            r.. value
        ____:
            r.. -1

    ___ put(self, key: i.., value: i..) -> N..:

        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)
        __ key n.. __ m:
            __ l..(deq) __ c:
                oldest  deq.popleft()
                del m[oldest]
        ____:
            deq.remove(key)

        m[key]  value
        deq.a..(key)
