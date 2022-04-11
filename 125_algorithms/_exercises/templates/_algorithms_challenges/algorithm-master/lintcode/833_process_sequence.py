c_ Solution:
    """
    @param logs: Sequence of processes
    @param queries: Sequence of queries
    @return: Return the number of processes
    """
    ___ numberOfProcesses  logs, queries
        t__    # list

        # 0: end, 1: start, 2: in progress
        ___ log __ logs:
            t__.a..((log.start, 1
            t__.a..((log.end + 1, 0

        ___ t __ queries:
            t__.a..((t, 2

        t__.s..()

        cnt 0
        time2cnt    # dict

        ___ t, status __ t__:
            __ status __ 0:
                cnt -_ 1
            ____ status __ 1:
                cnt += 1

            time2cnt[t] cnt

        r.. [time2cnt[t] ___ t __ queries]
