c_ Solution:
    """
    @param logs: Sequence of processes
    @param queries: Sequence of queries
    @return: Return the number of processes
    """
    ___ numberOfProcesses  logs, queries
        time    # list

        # 0: end, 1: start, 2: in progress
        ___ log __ logs:
            time.a..((log.start, 1))
            time.a..((log.end + 1, 0))

        ___ t __ queries:
            time.a..((t, 2))

        time.s..()

        cnt = 0
        time2cnt    # dict

        ___ t, status __ time:
            __ status __ 0:
                cnt -= 1
            ____ status __ 1:
                cnt += 1

            time2cnt[t] = cnt

        r.. [time2cnt[t] ___ t __ queries]
