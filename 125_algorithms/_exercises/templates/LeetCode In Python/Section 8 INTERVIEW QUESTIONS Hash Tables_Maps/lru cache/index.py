____ co.. ______ deque


c_ LRUCache:

    ___  -  capacity: __.
        .c _ capacity
        .m _ di..()
        .deq _ deque()

    ___ get key: __.)  __.:
        __ key __ .m:
            value _ .m[key]
            .deq.remove(key)
            .deq.ap..(key)
            r_ value
        ____
            r_ -1

    ___ put key: __., value: __.)  N..

        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)
        __ key no. __ .m:
            __ le.(.deq) __ .c:
                oldest _ .deq.popleft()
                del .m[oldest]
        ____
            .deq.remove(key)

        .m[key] _ value
        .deq.ap..(key)
