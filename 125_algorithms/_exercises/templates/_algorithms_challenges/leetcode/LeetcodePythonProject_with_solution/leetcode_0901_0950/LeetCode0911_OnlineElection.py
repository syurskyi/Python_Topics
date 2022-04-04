c_ TopVotedCandidate(o..

    ___ - , persons, times
        """
        :type persons: List[int]
        :type times: List[int]
        """
        arr    # list
        hashmap    # dict
        maxNum = 0
        maxP = N..
        ___ p, t __ z..(persons, times
            hashmap[p] = hashmap.g.. p, 0)+1
            __ hashmap[p] >= maxNum:
                maxP = p
                maxNum = hashmap[p]
            arr.a..([t, maxP])

    ___ q  t
        """
        :type t: int
        :rtype: int
        """
        i, j = 0, l..(arr)
        w.... i < j:
            mid = (i+j)//2
            __ t < arr[mid][0]:
                j = mid
            ____:
                i = mid+1
        r.. arr[i-1][1]


__ _____ __ _____
    candidate = TopVotedCandidate(
        [0,  1, 0, 1, 1],
        [24,29,31,76,81]
    )
    # [28],[24],[29],[77],[30],[25],[76],[75],[81],[80]
    print(candidate.q(28
    print(candidate.q(24
    print(candidate.q(29
    print(candidate.q(77
    print(candidate.q(30
    print(candidate.q(25
    print(candidate.q(76
    print(candidate.q(75
    print(candidate.q(81
    print(candidate.q(80
