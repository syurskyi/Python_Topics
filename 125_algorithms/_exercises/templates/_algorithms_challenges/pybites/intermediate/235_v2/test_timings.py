_______ p__

____ timings _______ timings_log, get_bite_with_fastest_avg_test


@p__.fixture(scope='module')
___ timings
    w__ open(timings_log) __ f:
        r.. f.readlines()


@p__.mark.parametrize("rows, expected_bites", [
    (50, '121'),
    (100, '169'),
    (150, '169'),
    (200, '46'),
    (250, ('60', '87')),
])
___ test_get_bite_with_fastest_avg_test(rows, expected_bites, timings):
    actual = s..(get_bite_with_fastest_avg_test(timings[:rows]))
    __ t..(expected_bites) __ tuple:
        ... actual __ expected_bites
    ____:
        ... actual __ expected_bites
