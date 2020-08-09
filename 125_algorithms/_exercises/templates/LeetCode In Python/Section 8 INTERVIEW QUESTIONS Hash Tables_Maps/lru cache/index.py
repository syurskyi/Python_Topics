from collections ______ deque


c_ LRUCache:

    ___ __init__(, capacity: int
        .c _ capacity
        .m _ dict()
        .deq _ deque()

    ___ get(, key: int) -> int:
        __ key __ .m:
            value _ .m[key]
            .deq.remove(key)
            .deq.append(key)
            r_ value
        ____
            r_ -1

    ___ put(, key: int, value: int) -> None:

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
        .deq.append(key)
