_______ d__

_______ p__

____ ? _______ ? ?
                    ?


?p__.f.. s.._"session"
___ pycon_events
    events ?
    r.. ?


?p__.f.. s.._"session"
___ filtered_pycons pycon_events
    filtered ? ?
    r.. ?


___ test_get_pycon_events_number pycon_events
    ... l.. ? __ 21


___ test_get_pycon_events_cities pycon_events
    a.. event.c.. ___ ? __ ?
    e.. {
        "Accra", "Belgrade", "Berlin",
        "Bratislava", "Cardiff", "Cleveland, OH", "Dublin",
        "Florence", "Hyderabad", "Jakarta", "Johannesburg",
        "Makati", "Munich", "Nairobi", "Odessa",
        "Ostrava", "Puerto Vallarta", "Sydney",
        "Taipei", "Toronto",
    }
    ... a.. __ e..


___ test_get_pycon_events_dates pycon_events
    ... a..(
        isi.. ev__.s.. d__.d__
        ___ event __ ?
    )
    ... a..(isi.. ev__.e.. d__.d__
               ___ event __ ?)


___ test_filter_pycons_number filtered_pycons
    a.. l.. ?
    e.. 9
    ... a.. __ e..


___ test_filter_pycons_cities filtered_pycons
    a.. ev__.city ___ ? __ ?
    e.. {
        "Belgrade", "Berlin", "Bratislava", "Cardiff",
        "Dublin", "Florence", "Munich", "Odessa",
        "Ostrava",
    }
    ... a.. __ e..


___ test_filter_pycons_dates filtered_pycons
    ... a..(
        isi.. ev__.s.. d__.d__
        ___ event __ ?
    )
    ... a..(
        isi.. ev__.e.. d__.d__
        ___ event __ ?
    )


___ test_filter_pycons_year filtered_pycons
    a.. pycon.s__.y.. ___ ? __ ?
    e.. {2019}
    ... a.. __ e..


___ test_filter_pycons_continent filtered_pycons
    a.. ? p__.c.. ___ ? __ ?
    e.. {"Europe"}
    ... a.. __ e..
