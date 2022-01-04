____ collections _______ Counter
____ d__ _______ date
____ unittest.mock _______ patch, MagicMock

_______ pytest

_______ monitor
____ monitor _______ timeit, ALERT_MSG


@pytest.fixture()
___ clean_cache
    """Make sure each test starts with a clean cache dict"""
    monitor.violations = Counter()


@patch('monitor.time', MagicMock(side_effect=[0, 2]))
___ test_one_operation_within_time(clean_cache, capfd):
    """1 operation took 2 seconds = ok"""
    with timeit
        p..
    output = capfd.readouterr()[0]
    ... n.. output


@patch('monitor.time', MagicMock(side_effect=[0, 2, 0, 3]))
___ test_two_operations_one_too_long(clean_cache, capfd):
    """2 operations, 1 took >= 3 seconds = still ok"""
    with timeit
        p..
    # this one took too long
    with timeit
        p..
    output = capfd.readouterr()[0]
    ... n.. output


@patch('monitor.time', MagicMock(side_effect=[0, 2, 0, 3, 0, 4]))
___ test_three_operations_two_too_long(clean_cache, capfd):
    """3 operations, 2 took >= 3 seconds = still ok"""
    # Note that each timeit call takes the next 2 elements of side_effect
    # = mocked start/end times in seconds
    with timeit
        p..
    with timeit
        p..
    with timeit
        p..
    output = capfd.readouterr()[0]
    ... n.. output


@patch('monitor.time', MagicMock(side_effect=[0, 2, 0, 3, 0, 4, 0, 5]))
___ test_four_operations_three_took_too_long(clean_cache, capfd):
    """4 operations, 3 tooks >= 3 seconds = NOT ok, prints ALERT"""
    with timeit
        p..
    with timeit
        p..
    with timeit
        p..
    with timeit
        p..
    output = capfd.readouterr()[0]
    ... output.s.. __ ALERT_MSG


@patch('monitor.time', MagicMock(
    side_effect=[0, 2.3, 0, 3.3, 0, 2.1, 0, 2.21]
))
___ test_four_operations_three_took_too_long_using_floats(clean_cache, capfd):

    """4 operations, 3 tooks > 2.2 seconds = NOT ok, prints ALERT"""
    with timeit
        p..
    with timeit
        p..
    with timeit
        p..
    with timeit
        p..
    output = capfd.readouterr()[0]
    ... output.s.. __ ALERT_MSG


@patch('monitor.time', MagicMock(side_effect=[0, 3, 0, 3, 0, 4, 0, 5]))
___ test_four_operations_took_too_long_but_on_two_days(clean_cache, capfd):
    """4 tooks >= 3 seconds, but spread over 2 days = ok / no alert"""
    # 2 violations yesterday
    with patch('monitor.get_today', return_value=date(2018, 5, 1)):
        with timeit
            p..
        with timeit
            p..
    # 2 violations today
    with patch('monitor.get_today', return_value=date(2018, 5, 2)):
        with timeit
            p..
        with timeit
            p..
    output = capfd.readouterr()[0]
    ... n.. output
