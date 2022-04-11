_______ d__

_______ p__

____ pycons _______ (get_pycon_events, filter_pycons,
                    get_continent)


?p__.f..(scope="session")
___ pycon_events
    events get_pycon_events()
    r.. events


?p__.f..(scope="session")
___ filtered_pycons(pycon_events
    filtered filter_pycons(pycon_events)
    r.. filtered


___ test_get_pycon_events_number(pycon_events
    ... l..(pycon_events) __ 21


___ test_get_pycon_events_cities(pycon_events
    a.. {event.city ___ event __ pycon_events}
    e.. {
        "Accra", "Belgrade", "Berlin",
        "Bratislava", "Cardiff", "Cleveland, OH", "Dublin",
        "Florence", "Hyderabad", "Jakarta", "Johannesburg",
        "Makati", "Munich", "Nairobi", "Odessa",
        "Ostrava", "Puerto Vallarta", "Sydney",
        "Taipei", "Toronto",
    }
    ... a.. __ e..


___ test_get_pycon_events_dates(pycon_events
    ... a..(
        isi..(event.start_date, d__.d__)
        ___ event __ pycon_events
    )
    ... a..(isi..(event.end_date, d__.d__)
               ___ event __ pycon_events)


___ test_filter_pycons_number(filtered_pycons
    a.. l..(filtered_pycons)
    e.. 9
    ... a.. __ e..


___ test_filter_pycons_cities(filtered_pycons
    a.. {event.city ___ event __ filtered_pycons}
    e.. {
        "Belgrade", "Berlin", "Bratislava", "Cardiff",
        "Dublin", "Florence", "Munich", "Odessa",
        "Ostrava",
    }
    ... a.. __ e..


___ test_filter_pycons_dates(filtered_pycons
    ... a..(
        isi..(event.start_date, d__.d__)
        ___ event __ filtered_pycons
    )
    ... a..(
        isi..(event.end_date, d__.d__)
        ___ event __ filtered_pycons
    )


___ test_filter_pycons_year(filtered_pycons
    a.. {pycon.start_date.year ___ pycon __ filtered_pycons}
    e.. {2019}
    ... a.. __ e..


___ test_filter_pycons_continent(filtered_pycons
    a.. {get_continent(pycon.country) ___ pycon __ filtered_pycons}
    e.. {"Europe"}
    ... a.. __ e..