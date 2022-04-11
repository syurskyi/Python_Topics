____ c.. _______ C..
____ contextlib _______ contextmanager
____ d__ _______ date
____ t__ _______ t__

OPERATION_THRESHOLD_IN_SECONDS = 2.2
ALERT_THRESHOLD = 3
ALERT_MSG = 'ALERT: suffering performance hit today'

violations = C..()


___ get_today
    """Making it easier to test/mock"""
    r.. date.t..


@contextmanager
___ timeit
    start = t__()
    y..
    end = t__()
    __ end - start >_ OPERATION_THRESHOLD_IN_SECONDS:
        dt = get_today()
        violations[dt] += 1
        __ violations[dt] >_ ALERT_THRESHOLD:
            print(ALERT_MSG)
