c_ Solution o..
    ___ canReorderDoubled  A
        """
        :type A: List[int]
        :rtype: bool
        """
        v_map  # dict
        A.sort(k.._l... x: abs(x))
        ___ n __ A:
            v_map[n] = v_map.get(n, 0) + 1
        ___ n __ A:
            __ v_map[n] <= 0:
                c_
            __ 2 * n __ v_map and v_map[2 * n] > 0:
                v_map[n] -= 1
                v_map[2 * n] -= 1
            ____
                r_ F..
        r_ T..


__ ____ __ ____
    s  ?
    print s.canReorderDoubled([3, 1, 3, 6])
    print s.canReorderDoubled([2, 1, 2, 6])
    print s.canReorderDoubled([4, -2, 2, -4])
    print s.canReorderDoubled([1, 2, 4, 16, 8, 4])
