# Merge Intervals
# Question: Given a collection of intervals, merge all overlapping intervals.
# For example:
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
# Solutions:


c_ Interval:
    ___  -(self, s_0, e_0):
        start _ s
        end _ e
    ___ printIn(self,i):
        print ("[%d ,%d]"%(i.start,i.end))


c_ Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    ___ merge(self, intervals):
        intervals.sort(key _ lambda x:x.start)
        length_len(intervals)
        res_  # list
        ___ i __ ra..(length):
            __ res__  # list:
                res.ap..(intervals[i])
            ____
                size_len(res)
                __ res[size-1].start<_intervals[i].start<_res[size-1].end:
                    res[size-1].end_ma.(intervals[i].end, res[size-1].end)
                ____
                    res.ap..(intervals[i])
        r_ res


i1 _ Interval(1,3)
i2 _ Interval(2,6)
i3 _ Interval(8,10)
i4 _ Interval(15,18)
result _ Solution().merge([i1,i2,i3,i4])
___ i __ result:
    Interval().printIn(i)