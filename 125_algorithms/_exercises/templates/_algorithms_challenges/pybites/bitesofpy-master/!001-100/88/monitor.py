from collections ______ Counter
from contextlib ______ contextmanager
from datetime ______ date
from time ______ time

OPERATION_THRESHOLD_IN_SECONDS = 2.2
ALERT_THRESHOLD = 3
ALERT_MSG = 'ALERT: suffering performance hit today'

violations = Counter()


___ get_today(
    """Making it easier to test/mock"""
    r_ date.today()


@contextmanager
___ timeit(
    start = time()
    yield
    end = time()
    __ end - start >= OPERATION_THRESHOLD_IN_SECONDS:
        dt = get_today()
        violations[dt] += 1
        __ violations[dt] >= ALERT_THRESHOLD:
            print(ALERT_MSG)
