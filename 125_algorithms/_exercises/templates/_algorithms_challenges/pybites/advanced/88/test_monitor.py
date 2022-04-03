____ c.. _______ C..
____ d__ _______ date
____ unittest.mock _______ patch, MagicMock

_______ p__

_______ monitor
____ monitor _______ timeit, ALERT_MSG


?p__.f..()
___ clean_cache
    """Make sure each test starts with a clean cache dict"""
    monitor.violations = C..()


@patch('monitor.time', MagicMock(side_effect=[0, 2]))
___ test_one_operation_within_time(clean_cache, capfd
    """1 operation took 2 seconds = ok"""
    w__ timeit
        p..
    output = ?.r .. 0]
    ... n.. output


@patch('monitor.time', MagicMock(side_effect=[0, 2, 0, 3]))
___ test_two_operations_one_too_long(clean_cache, capfd
    """2 operations, 1 took >= 3 seconds = still ok"""
    w__ timeit
        p..
    # this one took too long
    w__ timeit
        p..
    output = ?.r .. 0]
    ... n.. output


@patch('monitor.time', MagicMock(side_effect=[0, 2, 0, 3, 0, 4]))
___ test_three_operations_two_too_long(clean_cache, capfd
    """3 operations, 2 took >= 3 seconds = still ok"""
    # Note that each timeit call takes the next 2 elements of side_effect
    # = mocked start/end times in seconds
    w__ timeit
        p..
    w__ timeit
        p..
    w__ timeit
        p..
    output = ?.r .. 0]
    ... n.. output


@patch('monitor.time', MagicMock(side_effect=[0, 2, 0, 3, 0, 4, 0, 5]))
___ test_four_operations_three_took_too_long(clean_cache, capfd
    """4 operations, 3 tooks >= 3 seconds = NOT ok, prints ALERT"""
    w__ timeit
        p..
    w__ timeit
        p..
    w__ timeit
        p..
    w__ timeit
        p..
    output = ?.r .. 0]
    ... output.s.. __ ALERT_MSG


@patch('monitor.time', MagicMock(
    side_effect=[0, 2.3, 0, 3.3, 0, 2.1, 0, 2.21]
))
___ test_four_operations_three_took_too_long_using_floats(clean_cache, capfd

    """4 operations, 3 tooks > 2.2 seconds = NOT ok, prints ALERT"""
    w__ timeit
        p..
    w__ timeit
        p..
    w__ timeit
        p..
    w__ timeit
        p..
    output = ?.r .. 0]
    ... output.s.. __ ALERT_MSG


@patch('monitor.time', MagicMock(side_effect=[0, 3, 0, 3, 0, 4, 0, 5]))
___ test_four_operations_took_too_long_but_on_two_days(clean_cache, capfd
    """4 tooks >= 3 seconds, but spread over 2 days = ok / no alert"""
    # 2 violations yesterday
    w__ patch('monitor.get_today', return_value=date(2018, 5, 1)):
        w__ timeit
            p..
        w__ timeit
            p..
    # 2 violations today
    w__ patch('monitor.get_today', return_value=date(2018, 5, 2)):
        w__ timeit
            p..
        w__ timeit
            p..
    output = ?.r .. 0]
    ... n.. output
