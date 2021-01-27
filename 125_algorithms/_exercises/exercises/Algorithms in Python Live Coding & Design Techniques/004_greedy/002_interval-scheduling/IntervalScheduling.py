
___ schedule(intervals
    optimal_interval_set = []

    #sorted(intervals, key=intervals[1])

    intervals.sort(key=lambda i: i[1])

    last_finish_time = float('-inf')

    ___ interval __ intervals:

        start = interval[0]

        __ start > last_finish_time:
            end = interval[1]

            optimal_interval_set.ap..(interval)

            last_finish_time = end

    r_ optimal_interval_set


intervals = [
    [0, 3],
    [0, 15],
    [5, 10],
    [7, 12],
    [11, 16],
    [12, 14],
    [16, 20],
]

optimal_schedule = schedule(intervals)

___ ele __ optimal_schedule:
    ___ i __ ra__(le_(ele)):
        print(ele[i])
    print()
