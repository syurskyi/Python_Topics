'''
Created on Oct 29, 2017

@author: MT
'''
_______ b__

c_ RangeModule(o..

    ___ -
        X [0, 10**9]
        track [F..]*2
    
    ___ addRangeHelper  left, right, track=T..
        ___ i.. x
            i b__.bisect_left(X, x)
            __ X[i] !_ x:
                X.insert(i, x)
                track.insert(i, track[i-1])
            r.. i
        i i.. left)
        j i.. right)
        X[i:j] [left]
        track[i:j] [track]

    ___ addRange  left, right
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        addRangeHelper(left, right, T..)

    ___ queryRange  left, right
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        i b__.b__(X, left)-1
        j b__.bisect_left(X, right)
        r.. a..(track[i:j])

    ___ removeRange  left, right
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        addRangeHelper(left, right, F..)

c_ Interval(o..
    ___ - , left, right
        left left
        right right

c_ RangeModule_own(o..
    ___ -
        intervals    # list

    ___ addRange  left, right
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        newInterval Interval(left, right)
        res    # list
        ___ interval __ intervals:
            __ newInterval.right < interval.left:
                res.a..(newInterval)
                newInterval interval
            ____ interval.right < newInterval.left:
                res.a..(interval)
            ____
                newInterval Interval(m..(interval.left, newInterval.left),\
                                    m..(interval.right, newInterval.right
        res.a..(newInterval)
        intervals res

    ___ queryRange  left, right
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        newInterval Interval(left, right)
        l, r 0, l..(intervals)-1
        w.... l <_ r:
            mid (l+r)//2
            __ intervals[mid].left >_ newInterval.right:
                r mid-1
            ____ intervals[mid].right <_ newInterval.left:
                l mid+1
            ____
                r.. intervals[mid].left <_ newInterval.left a..\
                    intervals[mid].right >_ newInterval.right
        r.. F..

    ___ removeRange  left, right
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        newInterval Interval(left, right)
        res    # list
        ___ interval __ intervals:
            __ newInterval.right >_ interval.right a.. newInterval.left <_ interval.left:
                _____
            ____ newInterval.right <_ interval.right a.. newInterval.left >_ interval.left:
                __ interval.left !_ newInterval.left:
                    res.a..(Interval(interval.left, newInterval.left
                __ interval.right !_ newInterval.right:
                    res.a..(Interval(newInterval.right, interval.right
            ____ newInterval.right <_ interval.left o. interval.right <_ newInterval.left:
                res.a..(interval)
            ____ newInterval.right <_ interval.right:
                tmpInterval Interval(newInterval.right, interval.right)
                __ tmpInterval.left < tmpInterval.right:
                    res.a..(tmpInterval)
            ____ newInterval.left >_ interval.left:
                tmpInterval Interval(interval.left, newInterval.left)
                __ tmpInterval.left < tmpInterval.right:
                    res.a..(tmpInterval)
        intervals res

__ _____ __ _____
#     rangeModule = RangeModule()
#     rangeModule.addRange(10, 20)
#     rangeModule.removeRange(14, 16)
#     print(rangeModule.queryRange(10, 14))
#     print(rangeModule.queryRange(13, 15))
#     print(rangeModule.queryRange(16, 17))
    
#     rangeModule = RangeModule()
#     print(rangeModule.addRange(6,8))
#     print(rangeModule.removeRange(7,8))
#     print(rangeModule.removeRange(8,9))
#     print(rangeModule.addRange(8,9))
#     print(rangeModule.removeRange(1,3))
#     print(rangeModule.addRange(1,8))
#     print(rangeModule.queryRange(2,4))
#     print(rangeModule.queryRange(2,9))
#     print(rangeModule.queryRange(4,6))

#     rangeModule = RangeModule()
#     print(rangeModule.queryRange(21,34))
#     print(rangeModule.queryRange(27,87))
#     print(rangeModule.addRange(44,53))
#     print(rangeModule.addRange(69,89))
#     print(rangeModule.queryRange(23,26))
#     print(rangeModule.queryRange(80,84))
#     print(rangeModule.queryRange(11,12))
#     print(rangeModule.removeRange(86,91))
#     print(rangeModule.addRange(87,94))
#     print(rangeModule.removeRange(34,52))
#     print(rangeModule.addRange(1,59))
#     print(rangeModule.removeRange(62,96))
#     print(rangeModule.removeRange(34,83))
#     print(rangeModule.queryRange(11,59))
#     print(rangeModule.queryRange(59,79))
#     print(rangeModule.queryRange(1,13))
#     print(rangeModule.queryRange(21,23))
#     print(rangeModule.removeRange(9,61))
#     print(rangeModule.addRange(17,21))
#     print(rangeModule.removeRange(4,8))
#     print(rangeModule.queryRange(19,25))
#     print(rangeModule.addRange(71,98))
#     print(rangeModule.addRange(23,94))
#     print(rangeModule.removeRange(58,95))
#     print(rangeModule.queryRange(12,78))
#     print(rangeModule.removeRange(46,47))
#     print(rangeModule.removeRange(50,70))
#     print(rangeModule.removeRange(84,91))
#     print(rangeModule.addRange(51,63))
#     print(rangeModule.removeRange(26,64))
#     print(rangeModule.addRange(38,87))
#     print(rangeModule.queryRange(41,84))
#     print(rangeModule.queryRange(19,21))
#     print(rangeModule.queryRange(18,56))
#     print(rangeModule.queryRange(23,39))
#     print(rangeModule.queryRange(29,95))
#     print(rangeModule.addRange(79,100))
#     print(rangeModule.removeRange(76,82))
#     print(rangeModule.addRange(37,55))
#     print(rangeModule.addRange(30,97))
#     print(rangeModule.addRange(1,36))
#     print(rangeModule.queryRange(18,96))
#     print(rangeModule.removeRange(45,86))
#     print(rangeModule.addRange(74,92))
#     print(rangeModule.queryRange(27,78))
#     print(rangeModule.addRange(31,35))
#     print(rangeModule.queryRange(87,91))
#     print(rangeModule.removeRange(37,84))
#     print(rangeModule.removeRange(26,57))
#     print(rangeModule.addRange(65,87))
#     print(rangeModule.addRange(76,91))
#     print(rangeModule.queryRange(37,77))
#     print(rangeModule.queryRange(18,66))
#     print(rangeModule.addRange(22,97))
#     print(rangeModule.addRange(2,91))
#     print(rangeModule.removeRange(82,98))
#     print(rangeModule.removeRange(41,46))
#     print(rangeModule.removeRange(6,78))
#     print(rangeModule.queryRange(44,80))
#     print(rangeModule.removeRange(90,94))
#     print(rangeModule.removeRange(37,88))
#     print(rangeModule.addRange(75,90))
#     print(rangeModule.queryRange(23,37))
#     print(rangeModule.removeRange(18,80))
#     print(rangeModule.addRange(92,93))
#     print(rangeModule.addRange(3,80))
#     print(rangeModule.queryRange(68,86))
#     print(rangeModule.removeRange(68,92))
#     print(rangeModule.queryRange(52,91))
#     print(rangeModule.addRange(43,53))
#     print(rangeModule.addRange(36,37))
#     print(rangeModule.addRange(60,74))
#     print(rangeModule.addRange(4,9))
#     print(rangeModule.addRange(44,80))
#     print(rangeModule.removeRange(85,93))
#     print(rangeModule.removeRange(56,83))
#     print(rangeModule.addRange(9,26))
#     print(rangeModule.queryRange(59,64))
#     print(rangeModule.queryRange(16,66))
#     print(rangeModule.removeRange(29,36))
#     print(rangeModule.removeRange(51,96))
#     print(rangeModule.removeRange(56,80))
#     print(rangeModule.addRange(13,87))
#     print(rangeModule.queryRange(42,72))
#     print(rangeModule.removeRange(6,56))
#     print(rangeModule.queryRange(24,53))
#     print(rangeModule.addRange(43,71))
#     print(rangeModule.removeRange(36,83))
#     print(rangeModule.removeRange(15,45))
#     print(rangeModule.queryRange(10,48))

    rangeModule RangeModule()
    print(rangeModule.addRange(55,62
    print(rangeModule.addRange(1,29
    print(rangeModule.removeRange(18,49
    print(rangeModule.queryRange(6,98
    print(rangeModule.queryRange(59,71
    print(rangeModule.removeRange(40,45
    print(rangeModule.removeRange(4,58
    print(rangeModule.removeRange(57,69
    print(rangeModule.removeRange(20,30
    print(rangeModule.removeRange(1,40
    print(rangeModule.queryRange(73,93
    print(rangeModule.removeRange(32,93
    print(rangeModule.addRange(38,100
    print(rangeModule.removeRange(50,64
    print(rangeModule.addRange(26,72
    print(rangeModule.queryRange(8,74
    print(rangeModule.queryRange(15,53
    print(rangeModule.addRange(44,85
    print(rangeModule.addRange(10,71
    print(rangeModule.queryRange(54,70
    print(rangeModule.removeRange(10,45
    print(rangeModule.queryRange(30,66
    print(rangeModule.addRange(47,98
    print(rangeModule.queryRange(1,7
    print(rangeModule.removeRange(44,78
    print(rangeModule.removeRange(31,49
    print(rangeModule.addRange(62,63
    print(rangeModule.addRange(49,88
    print(rangeModule.removeRange(47,72
    print(rangeModule.removeRange(8,50
    print(rangeModule.removeRange(49,79
    print(rangeModule.addRange(31,47
    print(rangeModule.addRange(54,87
    print(rangeModule.queryRange(77,78
    print(rangeModule.queryRange(59,100
    print(rangeModule.queryRange(8,9
    print(rangeModule.queryRange(50,51
    print(rangeModule.queryRange(67,93
    print(rangeModule.removeRange(25,86
    print(rangeModule.removeRange(8,92
    print(rangeModule.queryRange(31,87
    print(rangeModule.addRange(90,95
    print(rangeModule.addRange(28,56
    print(rangeModule.addRange(10,42
    print(rangeModule.queryRange(27,34
    print(rangeModule.addRange(75,81
    print(rangeModule.addRange(17,63
    print(rangeModule.removeRange(78,90
    print(rangeModule.addRange(9,18
    print(rangeModule.queryRange(51,74
    print(rangeModule.removeRange(20,54
    print(rangeModule.addRange(35,72
    print(rangeModule.queryRange(2,29
    print(rangeModule.addRange(28,41
    print(rangeModule.addRange(17,95
    print(rangeModule.addRange(73,75
    print(rangeModule.queryRange(34,43
    print(rangeModule.addRange(57,96
    print(rangeModule.queryRange(51,72
    print(rangeModule.removeRange(21,67
    print(rangeModule.removeRange(40,73
    print(rangeModule.removeRange(14,26
    print(rangeModule.removeRange(71,86
    print(rangeModule.queryRange(34,41
    print(rangeModule.removeRange(10,25
    print(rangeModule.queryRange(27,68
    print(rangeModule.queryRange(18,32
    print(rangeModule.removeRange(30,31
    print(rangeModule.queryRange(45,61
    print(rangeModule.addRange(64,66
    print(rangeModule.addRange(18,93
    print(rangeModule.queryRange(13,21
    print(rangeModule.removeRange(13,46
    print(rangeModule.removeRange(56,99
    print(rangeModule.queryRange(6,93
    print(rangeModule.addRange(25,36
    print(rangeModule.removeRange(27,88
    print(rangeModule.removeRange(82,83
    print(rangeModule.addRange(30,71
    print(rangeModule.addRange(31,73
    print(rangeModule.addRange(10,41
    print(rangeModule.queryRange(71,72
    print(rangeModule.queryRange(9,56
    print(rangeModule.addRange(22,76
    print(rangeModule.queryRange(38,74
    print(rangeModule.removeRange(2,77
    print(rangeModule.queryRange(33,61
    print(rangeModule.removeRange(74,75
    print(rangeModule.addRange(11,43
    print(rangeModule.queryRange(27,75
