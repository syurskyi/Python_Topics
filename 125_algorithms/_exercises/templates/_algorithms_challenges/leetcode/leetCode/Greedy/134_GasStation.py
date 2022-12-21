#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Refer to http://blog.csdn.net/kenden23/article/details/14106137


c.. Solution o..
    """
    Consider we start at gas station i, and until j we firstly run out of gas.

    That's say remain(i,j) = R(i) + ... + R(j) < 0, R(i) >= 0, R(j) < 0
    and remain(i, m) >= 0, where i =< m < j,
    We assume R(k) = gas(k) - cost(k) here.

    Further more, we can make sure remain(m+1, k) < 0.
    Just because remain(i,j) < 0 and remain(i, m) >= 0.
    So, next we just need to start from index k+1.

    So, firstly find all the (i,j) pairs, but just need to record the last j.
    Then if there is an unique(it's guaranteed) solution, it must be (j+1)
    """
    ___ canCompleteCircuit  gas, cost
        station_num = l..(gas)
        mark_station = -1
        all_remain = 0
        remain_gas = 0
        ___ i __ r..(station_num
            all_remain += (gas[i]-cost[i])
            remain_gas += (gas[i]-cost[i])
            __ remain_gas < 0:
                mark_station = i
                remain_gas = 0

        __ all_remain >= 0:
            r_ (mark_station + 1) % station_num
        ____
            r_ -1

        r_ -1

"""
[4]
[5]
[1,10,2,3,4,5,6]
[2,4,3,4,5,6,7]
[1,2,3,4,5,6,10]
[1,2,2,3,4,15,4]
[2,0,1,2,3,4,0]
[0,1,0,0,0,0,11]
"""
