____ c.. _______ C..
____ contextlib _______ contextmanager
____ d__ _______ date
____ time _______ time
_______ ___

OPERATION_THRESHOLD_IN_SECONDS = 2.2
ALERT_THRESHOLD = 3
ALERT_MSG = 'ALERT: suffering performance hit today'

violations = C..()


___ get_today
    """Making it easier to test/mock"""
    r.. date.t..


@contextmanager
___ timeit() __ N..
    start = time()
    ___
        y..
    finally:
        elapsed = time() - start
        __ elapsed > OPERATION_THRESHOLD_IN_SECONDS:
            violations.update([get_today()])
        __ violations[get_today()] >_ ALERT_THRESHOLD:
            print(ALERT_MSG)
        # print(f'{elapsed=}\n{len(violations)=}')
