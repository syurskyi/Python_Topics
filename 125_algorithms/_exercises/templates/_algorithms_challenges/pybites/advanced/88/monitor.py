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
    r.. date.t..


@contextmanager
___ timeit

    

    start_time = time()

    y.. 
    end_time = time()
    total_time = end_time - start_time
    __ total_time >_ OPERATION_THRESHOLD_IN_SECONDS:
        violations[get_today()] += 1
        __ violations[get_today()] >_ ALERT_THRESHOLD:
            print(ALERT_MSG)












