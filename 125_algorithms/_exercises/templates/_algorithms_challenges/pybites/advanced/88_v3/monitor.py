from collections import Counter
from contextlib import contextmanager
from datetime import date
from time import time
import sys

OPERATION_THRESHOLD_IN_SECONDS = 2.2
ALERT_THRESHOLD = 3
ALERT_MSG = 'ALERT: suffering performance hit today'

violations = Counter()


___ get_today():
    """Making it easier to test/mock"""
    return date.today()


@contextmanager
___ timeit() -> None:
    start = time()
    try:
        yield
    finally:
        elapsed = time() - start
        __ elapsed > OPERATION_THRESHOLD_IN_SECONDS:
            violations.update([get_today()])
        __ violations[get_today()] >= ALERT_THRESHOLD:
            print(ALERT_MSG)
        # print(f'{elapsed=}\n{len(violations)=}')
