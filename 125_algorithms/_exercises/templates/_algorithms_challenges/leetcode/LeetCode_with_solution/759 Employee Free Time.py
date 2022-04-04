#!/usr/bin/python3
"""
We are given a list schedule of employees, which represents the working time for
each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are
in sorted order.

Return the list of finite intervals representing common, positive-length free
time for all employees, also in sorted order.

Example 1:
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation:
There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.


Example 2:
Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]


(Even though we are representing Intervals in the form [x, y], the objects
inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1
, schedule[0][0].end = 2, and schedule[0][0][0] is not defined.)

Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero
length.

Note:

schedule and schedule[i] are lists with lengths in range [1, 50].
0 <= schedule[i].start < schedule[i].end <= 10^8.
"""
____ t___ _______ L..
_______ heapq


S = 0
E = 1


c_ Solution:
    ___ employeeFreeTime  schedule: L..[L..[L..[i..]]]) __ L..[L..[i..]]:
        """
        Method 1
        Looking at the head of each list through iterator
        Merge interval of heads, need to sort, then use heap
        After merge, find the open interval

        No need to merge, find the max end time, and compare to the min start time

        Method 2
        Better algorithm to find the open interval
        [s, e], we can think of this as two events: balance++ when time = s, and
        balance-- when time = e. We want to know the regions where balance == 0.

        Similar to meeting rooms II
        """
        cur_max_end = m..(
            itv[E]
            ___ itvs __ schedule
            ___ itv __ itvs
        )
        q    # list
        ___ i, itvs __ e..(schedule
            # head
            j = 0
            itv = itvs[j]
            heapq.heappush(q, (itv[S], i, j

        ret    # list
        w.... q:
            _, i, j = heapq.heappop(q)
            itv = schedule[i][j]
            __ cur_max_end < itv[S]:
                ret.a..([cur_max_end, itv[S]])

            cur_max_end = m..(cur_max_end, itv[E])

            # next
            j += 1
            __ j < l..(schedule[i]
                itv = schedule[i][j]
                heapq.heappush(q, (itv[S], i, j

        r.. ret

    ___ employeeFreeTime  schedule: L..[L..[L..[i..]]]) __ L..[L..[i..]]:
        """
        Method 2
        """
        # flatten the nested list
        lst    # list
        ___ itvs __ schedule:
            ___ itv __ itvs:
                lst.a..([itv[S], S])
                lst.a..([itv[E], E])

        lst.s..()
        count = 0
        prev = N..
        ret    # list
        ___ t, flag __ lst:
            __ count __ 0 a.. prev:
                ret.a..([prev, t])

            __ flag __ S:
                count += 1
            ____
                prev = t
                count -= 1

        r.. ret

    ___ employeeFreeTime_error  schedule: L..[L..[L..[i..]]]) __ L..[L..[i..]]:
        """
        Cannot store iterator in the heap to compare
        use index instead
        """
        schedules = l.. m..(i.., schedule
        cur_max_end = m..(
            itv[E]
            ___ emp __ schedule
            ___ itv __ emp
        )
        q    # list
        ___ emp_iter __ schedules:
            itv = next(emp_iter, N..)
            __ itv:
                heapq.heappush(q, (itv[S], itv, emp_iter

        ret    # list
        w.... q:
            _, itv, emp_iter = heapq.heappop(q)
            __ cur_max_end < itv[S]:
                ret.a..([cur_max_end, itv[S]])
            cur_max_end = m..(cur_max_end, itv[E])
            itv = next(emp_iter, N..)
            __ itv:
                heapq.heappush(q, (itv[S], itv, emp_iter

        r.. ret


__ _______ __ _______
    ... Solution().employeeFreeTime([[[1,2],[5,6]],[[1,3]],[[4,10]]]) __ [[3,4]]
    ... Solution().employeeFreeTime([[[4,16],[31,36],[42,50],[80,83],[95,96]],[[4,13],[14,19],[37,53],[64,66],[85,89]],[[17,24],[38,39],[49,51],[62,67],[79,81]],[[9,15],[17,24],[45,63],[65,68],[87,88]],[[17,33],[39,41],[43,57],[58,63],[70,84]]]) __ [[36, 37], [68, 70], [84, 85], [89, 95]]
