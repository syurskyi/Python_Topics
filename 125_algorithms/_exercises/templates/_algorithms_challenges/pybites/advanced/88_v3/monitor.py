____ c.. _______ C..
____ con.._______ c..
____ d__ _______ d__
____ t__ _______ t__
_______ ___

OPERATION_THRESHOLD_IN_SECONDS 2.2
ALERT_THRESHOLD 3
ALERT_MSG 'ALERT: suffering performance hit today'

violations C..()


___ get_today
    """Making it easier to test/mock"""
    r.. date.t..


@contextmanager
___ timeit() __ N..
    start t__
    ___
        y..
    _______
        elapsed t__ - start
        __ elapsed > OPERATION_THRESHOLD_IN_SECONDS:
            violations.update([get_today()])
        __ violations[get_today()] >_ ALERT_THRESHOLD:
            print(ALERT_MSG)
        # print(f'{elapsed=}\n{len(violations)=}')
