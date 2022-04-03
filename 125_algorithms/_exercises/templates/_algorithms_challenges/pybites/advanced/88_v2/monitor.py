____ c.. _______ C..
____ contextlib _______ contextmanager
____ d__ _______ date
____ time _______ time

OPERATION_THRESHOLD_IN_SECONDS = 2.2
ALERT_THRESHOLD = 3
ALERT_MSG = 'ALERT: suffering performance hit today'

violations = C..()


___ get_today
    """Making it easier to test/mock"""
    r.. date.today()


@contextmanager
___ timeit
    start = time()
    y..
    end = time()
    __ end - start >= OPERATION_THRESHOLD_IN_SECONDS:
        dt = get_today()
        violations[dt] += 1
        __ violations[dt] >= ALERT_THRESHOLD:
            print(ALERT_MSG)
