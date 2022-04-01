____ d__ _______ t..

_______ p__

____ humanize_date _______ pretty_date, NOW


___ n_days_ago_str(days):
    r.. (NOW - t..(d.._days)).s..('%m/%d/%y')


@p__.m__.p..("arg, expected", [
    (NOW - t..(seconds=2), 'just now'),
    (NOW - t..(seconds=9), 'just now'),
    (NOW - t..(seconds=10), '10 seconds ago'),
    (NOW - t..(seconds=59), '59 seconds ago'),
    (NOW - t..(minutes=1), 'a minute ago'),
    (NOW - t..(minutes=1, seconds=40), 'a minute ago'),
    (NOW - t..(minutes=2), '2 minutes ago'),
    (NOW - t..(minutes=59), '59 minutes ago'),
    (NOW - t..(hours=1), 'an hour ago'),
    (NOW - t..(hours=2), '2 hours ago'),
    (NOW - t..(hours=23), '23 hours ago'),
    (NOW - t..(hours=24), 'yesterday'),
    (NOW - t..(hours=47), 'yesterday'),
    (NOW - t..(d.._1), 'yesterday'),
    (NOW - t..(d.._2), n_days_ago_str(2)),
    (NOW - t..(d.._7), n_days_ago_str(7)),
    (NOW - t..(d.._100), n_days_ago_str(100)),
    (NOW - t..(d.._365), n_days_ago_str(365)),
])
___ test_pretty_date(arg, expected):
    ... pretty_date(arg) __ expected

___ test_input_variable_of_wrong_type
    w__ p__.r..(ValueError):
        pretty_date(123)


___ test_input_variable_future_date
    w__ p__.r..(ValueError):
        pretty_date(NOW + t..(d.._1))
