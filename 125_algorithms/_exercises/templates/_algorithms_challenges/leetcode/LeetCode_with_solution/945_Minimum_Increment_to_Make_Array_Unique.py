c_ Solution o..
    ___ minIncrementForUnique  A
        """
        :type A: List[int]
        :rtype: int
        """
        __ A is N.. or l.. A) __ 0:
            r_ 0
        res = 0
        num_set = s..()
        duplicate =    # list
        A.s..
        left, right = A[0], A[-1]
        holes = right - left + 1
        ___ v __ A:
            __ v __ num_set:
                duplicate.append(v)
            ____
                num_set.add(v)
        holes = holes - l.. num_set)
        # find a hole for these numbers
        ___ hole __ r.. left + 1, right
            __ holes __ 0 or l.. duplicate) __ 0:
                ______
            __ hole n.. __ num_set a.. hole > duplicate[0]:
                res += hole - duplicate.pop(0)
                holes -= 1
        w.. l.. duplicate) != 0:
            right += 1
            res += right - duplicate.pop(0)
        r_ res


__ ____ __ ____
    s  ?
    # print s.minIncrementForUnique([3, 2, 1, 2, 1, 7])
    # print s.minIncrementForUnique([0, 2, 2])
