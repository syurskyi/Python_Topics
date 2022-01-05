____ c.. _______ Counter
____ contextlib _______ contextmanager
____ d__ _______ date
____ time _______ time
_______ sys

OPERATION_THRESHOLD_IN_SECONDS = 2.2
ALERT_THRESHOLD = 3
ALERT_MSG = 'ALERT: suffering performance hit today'

violations = Counter()


___ get_today
    """Making it easier to test/mock"""
    r.. date.today()


@contextmanager
___ timeit() __ N..
    start = time()
    ___
        y..
    finally:
        elapsed = time() - start
        __ elapsed > OPERATION_THRESHOLD_IN_SECONDS:
            violations.update([get_today()])
        __ violations[get_today()] >= ALERT_THRESHOLD:
            print(ALERT_MSG)
        # print(f'{elapsed=}\n{len(violations)=}')
